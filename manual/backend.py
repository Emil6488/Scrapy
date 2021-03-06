import asyncio
from aiogram import Bot , Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import json

from requests.api import post
endpoint = "http://localhost:8000"

def getStarted(userId):
    responseRaw = requests.get(endpoint+ "/api/auto/start/"+str(userId))
    response = json.loads(responseRaw.content)
    return response

def end(userId):
    responseRaw = requests.get(endpoint+"/api/end/start/"+str(userId))
    if responseRaw.status_code == 200:
        return "Бот выключен"
    else:
        return "Ошибка сервера"


def formLink(userId):
    responseRaw = requests.get(endpoint + "/api/form/"+str(userId))
    response = json.loads(responseRaw.content)
    print(responseRaw.content)
    if responseRaw.status_code == 200:
        print(response['message'])
        val = '<a href="'+response['message']+'">Открыть ссылку</a>'
        return val
    else:
        return "Ошибка сервера"



def viewFilterValue(userId):
    responseRaw = requests.get(endpoint + "/api/parameters/"+str(userId))
    response = json.loads(responseRaw.content)
    if responseRaw.status_code == 200:      
        return f'Данные фильтра следующие:\n'\
                f'минимальная цена: {response["minPrice"]}\n'\
                f'максимальная цена: {response["maxPrice"]}\n'\
                f'минимальный год: {response["minYear"]}\n'\
                f'максимальный год: {response["maxYear"]}\n'\
                f'минимальный одометр: {response["minOdometer"]}\n'\
                f'максимальный одометр: {response["maxOdometer"]}\n'\
                f'кондиция: {response["condition"]}\n'\
                f'миля: {response["miles"]}\n'\
                f'почтовый индекс: {response["postalCode"]}\n'\
                f'модель машины: {response["carModel"]}\n'
    elif responseRaw.status_code == 404:
        return "Вы не активизировались"
    else: return "Ошибка сервера"

def carsEveryMinute():
    responseRaw = requests.get(endpoint + "/api/scrap/")
    if responseRaw.status_code == 405:
        return []
    else:
        return json.loads(responseRaw.content)
