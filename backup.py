@dp.message_handler(Text(equals="Последние 5 машин"))
async def get_last_five_cars(message:  types.Message):
    response = scrapMain(5,None)
    for v in response:
        cars = f"{hlink(v['title'], v['link'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['posted'])}\n" 
        await message.answer(cars)

@dp.message_handler(Text(equals="Последние 10 машин"))
async def get_last_ten_cars(message:  types.Message):
    response = scrapMain(10,None)
    for v in response:
        cars = f"{hlink(v['title'], v['link'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['posted'])}\n" 
        await message.answer(cars)

@dp.message_handler(Text(equals="Последние 25 машин"))
async def get_last_twentyfive_cars(message:  types.Message):
    response = scrapMain(25)
    for v in response:
        cars = f"{hlink(v['title'], v['link'])}\n"\
                f"{hcode(v['price'])}\n"\
                f"{hcode(v['posted'])}\n" 
        await message.answer(cars)

async def cars_every_minute():
    global userId
    while True:
        if userId is None:
            print("User id is not defined")
        else:
            await bot.send_message(userId, "Hello")
        await asyncio.sleep(10)