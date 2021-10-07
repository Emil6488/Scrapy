import asyncio
from functools import cache
from aiogram import Bot , Dispatcher, executor, types
from auth_data import token
import json
import datetime
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from scrapper import scrapMain, scrapDateAndQuery
from helper import checkDates


userId = None
maxPrice = None
minPrice = None
latestCar = None
search = False
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #start_buttons = [ "Последние 5 машин","Последние 10 машин","Последние 25 машин","Включить фильтр","Посмотреть детали фильтра", "Отключить фильтр","Фильтр (Помощь)"]
    global latestCar
    global userId
    start_buttons = ["Включить фильтр","Посмотреть детали фильтра", "Отключить фильтр","Фильтр (Помощь)"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    userId = message.from_user.id
    await message.answer("Добро пожаловать, ваш профиль сохранён. Нажмите кнопку внизу.")
    await message.answer("Отправляем вам 15 машин")
    response = scrapMain(5)
    for v in response:
        latestCar = checkDates(latestCar, v['posted'])
        cars = f"{hlink(v['title'], v['link'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['posted'])}\n" 
        await message.answer(cars) 
    await message.answer("Далее сообщения будут обновляться", reply_markup=keyboard)
    




@dp.message_handler(Text(equals="Включить фильтр"))
async def activateFilter(message:  types.Message):
    search=True
    await message.answer("Вводите критерии поиска")



@dp.message_handler(Text(equals="Посмотреть детали фильтра"))
async def get_search_details(message:  types.Message):
    await message.answer("Детали поиска")
    if maxPrice is None:
        await message.answer("Search: maxPrice is not defined")
    else:
        await message.answer("Search: maxPrice = "+maxPrice)
    if minPrice is None:
        await message.answer("Search: minPrice is not defined")
    else:
        await message.answer("Search: minPrice = "+minPrice)


@dp.message_handler(Text(equals="Отключить фильтр"))
async def disable_Filter(message:  types.Message):
    global search
    global maxPrice
    global minPrice
    maxPrice = None
    minPrice = None
    search = False
    await message.answer("Фильтр отключен")

@dp.message_handler(Text(contains="Search: "))
async def enter_Max_Price(message:  types.Message):
    global search
    global maxPrice
    global minPrice
    if search is True:
        condition = list(message.text.split(" "))
        criteria = condition[1]
        value = condition[2]
        if criteria == "maxPrice":
            maxPrice = value
        elif criteria == "minPrice":
            minPrice = value
        await message.answer("Вводите критерии")
    else:
        await message.answer("Пожалуйста включите фильтр")

@dp.message_handler(Text(equals="Фильтр (Помощь)"))
async def get_help(message:  types.Message):
    await message.answer("Для добавления специального критерия нажмите кнопку Редактировать поиск и далее наберите следующее:")
    await message.answer("Незабывайте пробелыи слово Search перед началом! Это важно")
    await message.answer("Search: maxPrice = число")
    await message.answer("Search: minPrice = число")


async def cars_every_minute():
    global userId
    global latestCar
    global search
    while True:
        if userId is None:
            print("User id is not defined")
        else:
            response = scrapDateAndQuery(latestCar,createQuery(),search)
            if len(response)==0:
                print("No new updates")
            else:
                latestCar = response[0]['posted']
                for v in response:
                    cars = f"{hlink(v['title'], v['link'])}\n"\
                        f"{hcode(v['price'])}\n"\
                        f"{hcode(v['posted'])}\n" 
                    await bot.send_message(userId, cars)
        await asyncio.sleep(10)

def createQuery():
    global maxPrice
    global minPrice
    query = "?"
    if maxPrice is not None:
        query = query + "maxPrice="+maxPrice+"&"
    if minPrice is not None:
        query = query + "minPrice="+value+"&"
    return query

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(cars_every_minute())
    executor.start_polling(dp)
