import requests
from bs4 import BeautifulSoup
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import json

endpoint = "https://8fe0-131-220-35-155.ngrok.io"

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
        return f"{hlink('Открыть ссылку', response['message'])}\n"
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