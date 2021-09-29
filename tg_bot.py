import asyncio
from aiogram import Bot , Dispatcher, executor, types
from auth_data import token ,  chat_id
import json
import datetime
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from main import check_cars_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все машины", "Последние 5 машин","Свежие машины"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer("Лента машин", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все машины"))
async def get_all_cars(message:  types.Message):
    with open("cars.json", encoding='utf-8') as file:
        new_cars = json.load(file)

    for k , v in sorted(new_cars.items()):
        cars = f"{hbold(datetime.datetime.fromtimestamp(v['date_timestamp']))}\n"\
               f"{hlink(v['name'], v['url'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['year'])}\n"
        await message.answer(cars)

@dp.message_handler(Text(equals="Последние 5 машин"))
async def get_last_cars(message:  types.Message):
    with open("cars.json", encoding='utf-8') as file:
        new_cars = json.load(file)

    for k , v in sorted(new_cars.items())[-5:]:
        cars = f"{hbold(datetime.datetime.fromtimestamp(v['date_timestamp']))}\n"\
               f"{hlink(v['name'], v['url'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['year'])}\n"        
        await message.answer(cars)

@dp.message_handler(Text(equals="Свежие машины"))
async def get_fresh_cars(message:  types.Message):
    fresh_car = check_cars_update()

    if len(fresh_car) >= 1:
        for k, v in sorted(fresh_car.items()):
            cars = f"{hbold(datetime.datetime.fromtimestamp(v['date_timestamp']))}\n" \
               f"{hlink(v['name'], v['url'])}\n" \
                f"{hcode(v['price'])}\n" \
                f"{hcode(v['year'])}\n" 
        await message.answer(cars)
    else:
        await message.answer("Пока нету новых машин....")

async def cars_every_minutes():
    while True:
        fresh_car = check_cars_update()
        if len(fresh_car) >= 1:
            for k, v in sorted(fresh_car.items()):
                cars = f"{hbold(datetime.datetime.fromtimestamp(v['date_timestamp']))}\n" \
                        f"{hlink(v['name'], v['url'])}\n" \
                        f"{hcode(v['price'])}\n" \
                        f"{hcode(v['year'])}\n"
                await bot.send_message(chat_id=chat_id)
        #else:
        #    await bot.send_message(user_id, "None")
        await asyncio.sleep(60)

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(cars_every_minutes())
    executor.start_polling(dp)