import asyncio
from functools import cache
from aiogram import Bot , Dispatcher, executor, types
from auth_data import token
import json
import datetime
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from scrapper import scrapMain, scrapDateAndQuery
from backend import getStarted, end, formLink, viewFilterValue
from helper import checkDates

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ["Включить","Выключить", "Фильтр (настр)","Фильтр (обзор)"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    userId = message.from_user.id
    await message.answer("Добро пожаловать, ваш профиль сохранён. Выберите режим внизу", reply_markup=keyboard)
    

@dp.message_handler(Text(equals="Включить"))
async def start(message: types.Message):
    userId = message.from_user.id
    response = getStarted(userId)
    for v in response:
        cars = f"{hlink(v['title'], v['link'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['posted'])}\n" 
        await message.answer(cars) 
    await message.answer("Далее сообщения будут обновляться")



@dp.message_handler(Text(equals="Включить"))
async def endMessages(message:  types.Message):
    userId = message.from_user.id
    response = end(userId)
    await message.answer(response)


@dp.message_handler(Text(equals="Фильтр (настр)"))
async def handleFilter(message:  types.Message):
    userId = message.from_user.id
    response = formLink(userId)
    await message.answer(response)

@dp.message_handler(Text(equals="Фильтр (обзор)"))
async def viewFilterValues(message:  types.Message):
    userId = message.from_user.id
    response = viewFilterValue(userId)
    await message.answer(response)


if __name__=='__main__':
    loop = asyncio.get_event_loop()
    #loop.create_task(cars_every_minute())
    executor.start_polling(dp)
