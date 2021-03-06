import asyncio
from functools import cache
from aiogram import Bot , Dispatcher, executor, types
from auth_data import token
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from backend import getStarted, end, formLink, viewFilterValue, carsEveryMinute
import schedule
import time


bot = Bot(token="2018151846:AAE0HhWs3OCntHLHTX4rhhf_aQkfACqe4fU", parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    start_buttons = ["Включить","Выключить", "Фильтр (настр)","Фильтр (обзор)"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    userId = message.from_user.id
    await message.answer("Добро пожаловать, По умолчанию вам будут отправлены машины из Лос Анджелеса")
    await message.answer("Включите", reply_markup=keyboard)

    

@dp.message_handler(Text(equals="Включить"))
async def start(message: types.Message):
    try:
        userId = message.from_user.id
        response = getStarted(userId)
        for v in response:
            cars = f"{hlink(v['title'], v['link'])}\n"\
                    f"{hcode(v['price'])}\n"\
                    f"{hcode(v['posted'])}\n" 
            await message.answer(cars) 
        await message.answer("Далее сообщения будут обновляться")
        loop = asyncio.get_event_loop()
        loop.create_task(cars_every_minute())
    except Exception as e:
        print(e)



@dp.message_handler(Text(equals="Выключить"))
async def endMessages(message:  types.Message):
    try:
        userId = message.from_user.id
        response = end(userId)
        await message.answer(response)
    except Exception as e:
        print(e)



@dp.message_handler(Text(equals="Фильтр (настр)"))
async def handleFilter(message:  types.Message):
    try:
        userId = message.from_user.id
        response = formLink(userId)
        print(response)
        await message.answer(response, parse_mode=types.ParseMode.HTML)
    except Exception as e:
        print(e)

@dp.message_handler(Text(equals="Фильтр (обзор)"))
async def viewFilterValues(message:  types.Message):
    try:
        userId = message.from_user.id
        response = viewFilterValue(userId)
        await message.answer(response)
    except Exception as e:
        print(e)


async def cars_every_minute():
    while True:
        try:    
            print("executed")
            response = carsEveryMinute()
            if isinstance(response, list):
                print("hello")
                continue
            for key in response:
                userId = key
                body = response[key]
                if isinstance(body, str):
                    print("no new data")
                    await bot.send_message(userId, body)
                    continue
                for v in body:
                    cars = f"{hlink(v['title'], v['link'])}\n"\
                            f"{hcode(v['price'])}\n"\
                            f"{hcode(v['posted'])}\n" 
                    await bot.send_message(userId, cars)
            await asyncio.sleep(120)
        except Exception as e:
            print(e)

if __name__=='__main__':    
    print("demo")
    executor.start_polling(dp)
    