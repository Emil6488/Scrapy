import requests
from bs4 import BeautifulSoup
from auto.helper import checkDates, findLatest
from auto.models import Auto
from datetime import datetime
from . import route

from itertools import cycle
import traceback




def returnPage(url):
    proxies = route.get_proxies()
    proxy_pool = cycle(proxies)
    for i in range(1,45):
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})
            print(response);
            return response
        except:
            print("Skipping. Connnection error")



def scrapMain(limit, userId,URL = "https://losangeles.craigslist.org/d/cars-trucks/search/cta", firstSearch = True):
    cars = []
    proxies = {
    "http": "http://10.10.1.10:1080",
    "https": "https://10.10.1.10:1080",
    }
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    searchResults = soup.find(id="search-results")
    carRows = searchResults.find_all("li", class_="result-row")
    counter = 0
    for car in carRows:
        url = car.find("a", href=True)
        price = url.find("span", class_="result-price")
        if price is None:
            parsedCar = scrapContent(url['href'],0, userId,firstSearch)
        else:
            parsedCar = scrapContent(url['href'], price.text, userId,firstSearch)        
        cars.append(parsedCar)
        limit = limit - 1
        if limit == 0:
            return cars

def scrapContent(link,price, userId,firstSearch):
    page = returnPage(link)
    soup = BeautifulSoup(page.content, "html.parser")
    #extract posted
    dateBar = soup.find("header", class_="dateReplyBar")
    time = dateBar.find("time", class_="date")
    posted = time.text.strip()
    #extract name
    attr = soup.find("div", class_="mapAndAttrs")
    name = attr.find("p", class_="attrgroup")
    title = name.text.strip()
    return setContent(title, link, price, posted, userId,firstSearch)


def setContent(title, link, price, posted, userId, firstSearch):
    print(posted)
    formatPosted = datetime.strptime(posted, '%Y-%d-%m  %H:%M')
    auto = Auto(link = link,title = title,price = price,posted = formatPosted,userId = userId)
    if firstSearch == True:
        print('inside')
        auto.save()
    return {
     "link":link,
     "title":title,
     "price":price,
     "posted":posted
    }


def generateQuery(parameter):
    query = ""
    if parameter.minPrice:
        query = query+"min_price="+str(parameter.minPrice)+"&"
    if parameter.maxPrice:
        query = query+"max_price="+str(parameter.maxPrice)+"&"
    if parameter.minYear:
        query = query+"min_auto_year="+str(parameter.minYear)+"&"
    if parameter.maxYear:
        query = query+"max_auto_year="+str(parameter.maxYear)+"&"
    if parameter.minOdometer:
        query = query+"min_auto_miles="+str(parameter.minOdometer)+"&"
    if parameter.maxOdometer:
        query = query+"max_auto_miles="+str(parameter.maxOdometer)+"&"
    if parameter.condition:
        query = query+"condition="+str(parameter.condition)+"&"
    if parameter.miles:
        query = query+"search_distance="+str(parameter.miles)+"&"
    if parameter.postalCode:
        query = query+"postal="+str(parameter.postalCode)+"&"
    if parameter.carModel:
        query = query+"auto_make_model="+parameter.carModel+"&"
    return query