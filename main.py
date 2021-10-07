import fake_useragent
import requests
from bs4 import BeautifulSoup, Tag as BS
import json
from datetime import datetime
import time
import lxml
from model_and_make import model_name_list
import os


def get_first_cars():
    user = fake_useragent.UserAgent().random
    
    headers = {
        'user-agent': user
    }

    url = 'https://losangeles.craigslist.org/d/cars-trucks/search/cta'
    r = requests.get(url=url, headers= headers)

    with open('index.html' , 'w', encoding='utf-8') as file:
        file.write(r.text)

    new_cars ={} 

    soup = BS(r.text, "lxml")
    car_card_list = []

    car_cards = soup.find_all('li', class_='result-row')

    for car_url in car_cards:
        car_url = car_url.find('a').get('href')
        car_card_list.append(car_url)

    for car in car_card_list:   
        r = requests.get(url=car, headers= headers)
    
        list = []
        soup = BS(r.text, "lxml")
        main_div = soup.find("div", class_='mapAndAttrs')
        main_price = soup.find('span', class_='price')
        data = soup.find('time', ).get('datetime')
        date_timestamp = datetime.strptime(data[0:19],"%Y-%m-%dT%H:%M:%S")
        a = main_div.find_all('span'.split())
        for index in a:
            c = index.text
            list.append(c)
        full_name = list[0]
        a = list[0].split()
        # находим год выпуск
        for y in a:
            if y.isnumeric():
                year = y
                if int(year) > 1900 and int(year) < 2100:
                    break
                else:
                    year = 'None'
                    continue 
        # конец года выпуска
        # ищен модель машины
        m = a[0]
        for m in a:
            if m.capitalize() in model_name_list:
                model_car = m
                break
            else:
                model_car = "None"
                continue

        # убираем параметр у которых нету знака ":"
        parametr_list = []
        for item in list:
            if ":" in item:
                parametr_list.append(item)

        # ищем параметров для машины
        parametr_dict = {(i.split(':')[0]):(i.split(':')[1]) for i in parametr_list}
        odometer = parametr_dict['odometer']
        title_status = parametr_dict['title status']

        car_id = car.split('/')[-1]
        car_id = car_id[:-5]

        new_cars[car_id] = {
                "full_name" : full_name,
                "date_timestamp" : date_timestamp,
                "url" : car,
                "name" : model_car.capitalize(),
                "price" : main_price.string(),
                "year" : year,
                'odometer' : odometer,
                'title_status' : title_status
            }
 
        with open('cars.json' , 'w', encoding='utf-8') as file:
            json.dump(new_cars, file, indent=4, ensure_ascii=False, default=str)  


def check_cars_update():

    if(os.stat("cars.json").st_size > 0):
        with open("cars.json", encoding="utf-8") as file:
            new_cars = json.load(file)
    else:
        new_cars = None
    
    user = fake_useragent.UserAgent().random
    
    headers = {
        'user-agent': user
    }

    url = 'https://losangeles.craigslist.org/d/cars-trucks/search/cta'
    r = requests.get(url=url, headers= headers)

    soup = BS(r.text, "lxml")
    car_cards = soup.find_all('li', class_='result-row')
    car_card_list = []
    for car_url in car_cards:
        car_url = car_url.find('a').get('href')
        car_card_list.append(car_url)
    
    fresh_car = {}
    for car in car_card_list:           
        car_id = car.split('/')[-1]
        car_id = car_id[:-5]
        #print(car_id)
        if car_id in new_cars:
            continue
        else:
            r = requests.get(url=car, headers= headers)
            list = []
            soup = BS(r.text, "lxml")
            main_div = soup.find("div", class_='mapAndAttrs')
            main_price = soup.find('span', class_='price')
            data = soup.find('time', ).get('datetime')
            date_timestamp = datetime.strptime(data[0:19],"%Y-%m-%dT%H:%M:%S")
            a = main_div.find_all('span'.split())
            for index in a:
                c = index.text
                list.append(c)
            full_name = list[0]
            a = list[0].split()
            # находим год выпуск
            for y in a:
                if y.isnumeric():
                    year = y
                    if int(year) > 1900 and int(year) < 2100:
                        break
                    else:
                        year = 'None'
                        continue 
            # конец года выпуска
            # ищен модель машины
            m = a[0]
            for m in a:
                if m.capitalize() in model_name_list:
                    model_car = m
                    break
                else:
                    model_car = "None"
                    continue

            # убираем параметр у которых нету знака ":"
            parametr_list = []
            for item in list:
                if ":" in item:
                    parametr_list.append(item)

            # ищем параметров для машины
            parametr_dict = {(i.split(':')[0]):(i.split(':')[1]) for i in parametr_list}
            if 'odometer' in parametr_dict.keys():
                odometer = parametr_dict['odometer']
            else:
                odometer = 0
            if 'title status' in parametr_dict.keys():
                title_status = parametr_dict['title status']
            else:
                title_status = 'Dont status'

            if isinstance(main_price, Tag):
                price = main_price.text
            else:
                price = "undefined"
            new_cars[car_id] = {
                'full_name' : full_name,
                "date_timestamp" : date_timestamp,
                "url" : car,
                "name" : model_car.capitalize(),
                "price" : price,
                "year" : year,
                'odometer' : odometer,
                'title_status' : title_status
            }

            fresh_car[car_id] = {
                "full_name" : full_name,
                "date_timestamp" : date_timestamp,
                "url" : car,
                "name" : model_car.capitalize(),
                "price" : price,
                "year" : year,
                'odometer' : odometer,
                'title_status' : title_status
            }
 
    with open('cars.json' , 'w', encoding='utf-8') as file:
        json.dump(new_cars, file, indent=4, ensure_ascii=False, default=str)  
    return fresh_car

def main():
    #get_first_cars()
    check_cars_update()


if __name__  == '__main__':
    main()