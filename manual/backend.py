import requests
from bs4 import BeautifulSoup
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import json

def getStarted(userId):
    responseRaw = requests.get("https://4385-78-48-84-207.ngrok.io/api/auto/start/"+str(userId))
    response = responseRaw.content
    print(response)       
    return json.loads(response)

def end(userId):
    responseRaw = requests.get("https://4385-78-48-84-207.ngrok.io/api/end/start/"+str(userId))
    if responseRaw.status_code == 200:
        return "Бот выключен"
    else:
        return "Ошибка сервера"


def formLink(userId):
    responseRaw = requests.get("https://4385-78-48-84-207.ngrok.io/api/parameters/")
    response = responseRaw.content
    if responseRaw.status_code == 200:
        return f"{hlink('Открыть ссылку', response['message'])}\n"
    else:
        return "Ошибка сервера"



def viewFilterValue(userId):
    responseRaw = requests.get("https://4385-78-48-84-207.ngrok.io/api/parameters/"+str(userId))
    response = responseRaw.content
    if responseRaw.status_code == 200:      
        return f'Данные фильтра следующие, минимальная цена {response["minPrice"]}\n'\
                f'Данные фильтра следующие, максимальная цена {response["maxPrice"]}\n'\
                f'Данные фильтра следующие, минимальный год {response["minYear"]}\n'\
                f'Данные фильтра следующие, максимальный год {response["maxYear"]}\n'\
                f'Данные фильтра следующие, минимальный одометр {response["minOdometer"]}\n'\
                f'Данные фильтра следующие, максимальный одометр {response["maxOdometer"]}\n'\
                f'Данные фильтра следующие, кондиция {response["condition"]}\n'\
                f'Данные фильтра следующие, миля {response["miles"]}\n'\
                f'Данные фильтра следующие, почтовый индекс {response["postalCode"]}\n'\
                f'Данные фильтра следующие, модель машины {response["carModel"]}\n'
    elif responseRaw.status_code == 404:
        return "Вы не активизировались"   
    else: return "Ошибка сервера"