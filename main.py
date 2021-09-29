import fake_useragent
import requests
from bs4 import BeautifulSoup as BS
import json
from datetime import datetime
import time
import lxml


def get_first_cars():
    user = fake_useragent.UserAgent().random
    
    headers = {
        'user-agent': user
    }

    url = 'https://losangeles.craigslist.org/d/cars-trucks/search/cta'
    r = requests.get(url=url, headers= headers)
    new_cars ={}
    if r.status_code ==200:
        soup = BS(r.text, "lxml")
        main_ul = soup.find("ul", id='search-results')
        li_list = main_ul.find_all("li", attrs={'class':'result-row'})
        for li in li_list:
            title = li.find('h3')
            href = title.a['href']
            name = li.find_next('a', class_='result-title hdrlnk').text.replace("*", " ")
            b = name.split()
            y = b[0]
            if y.isdigit():
                year = y
            else:
                for y in b:
                    if y.isnumeric():
                        year = y
                        if int(year) > 1900 and int(year) < 2100:
                            break
                        else:
                            year = 'None'
                            continue          
            a = li.find_next('div', attrs={'class': 'result-info'})
            price = a.find('span', class_='result-price').text
            data = li.find_next('time' ,class_ ='result-date').get('datetime')
            date_from_iso =datetime.fromisoformat(data)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d  %H:%M:%S")
            date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d  %H:%M:%S").timetuple())

            car_id = href.split('/')[-1]
            car_id = car_id[:-5]

            new_cars[car_id] = {
                "date_timestamp" : date_timestamp,
                "url" : href,
                "name" : name,
                "price" : price,
                "year" : year,
            }
        
        with open('cars.json' , 'w', encoding='utf-8') as file:
            json.dump(new_cars, file, indent=4, ensure_ascii=False)

def check_cars_update():

    with open("cars.json", encoding="utf-8") as file:
        new_cars = json.load(file)
    
    user = fake_useragent.UserAgent().random
    
    headers = {
        'user-agent': user
    }


    url = 'https://losangeles.craigslist.org/d/cars-trucks/search/cta'
    r = requests.get(url=url, headers= headers)

    
    soup = BS(r.text, "lxml")
    main_ul = soup.find("ul", id='search-results')
    li_list = main_ul.find_all("li", attrs={'class':'result-row'})

    fresh_car = {}
    for li in li_list:
        title = li.find('h3')
        href = title.a['href']
        car_id = href.split('/')[-1]
        car_id = car_id[:-5]
        if car_id in new_cars:
            continue
        else:
            name = li.find_next('a', class_='result-title hdrlnk').text
            b = name.split()
            y = b[0]
            year = 'None'
            if y.isdigit():
                if (int(y) > 1900 and int(y) < 2100):
                     year = y
                else:
                    year = 'None'
            else:
                for y in b:
                    if y.isnumeric():
                        year = y
                        if int(year) > 1900 and int(year) < 2100:
                            break
                        else:
                            year = 'None'
                            continue         
            a = li.find_next('div', attrs={'class': 'result-info'})
            price = a.find('span', class_='result-price').text
            data = li.find_next('time' ,class_ ='result-date').get('datetime')
            date_from_iso =datetime.fromisoformat(data)
            date_time = datetime.strftime(date_from_iso, "%Y-%m-%d  %H:%M:%S")
            date_timestamp = time.mktime(datetime.strptime(date_time, "%Y-%m-%d  %H:%M:%S").timetuple())

            new_cars[car_id] = {
                "date_timestamp" : date_timestamp,
                "url" : href,
                "name" : name,
                "price" : price,  
                'year' : year              
                }

            fresh_car[car_id] = {
                "date_timestamp" : date_timestamp,
                "url" : href,
                "name" : name,
                "price" : price,
                'year': year
                }

    with open("cars.json" , 'w', encoding="utf-8") as file:
        json.dump(new_cars, file , indent=4, ensure_ascii=False)
    
    return fresh_car

def main():
    #get_first_cars()
    check_cars_update()


if __name__  == '__main__':
    main()