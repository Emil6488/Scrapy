import requests
from bs4 import BeautifulSoup
from auto.models import Auto
from datetime import datetime
from itertools import cycle
from parameters.models import Parameters
import logging
import fake_useragent

logger = logging.getLogger('error_logger')

user = fake_useragent.UserAgent().random
    
headers = {
        'user-agent': user
}

def scrapMain(limit, userId,URL = "https://losangeles.craigslist.org/d/cars-trucks/search/cta", firstSearch = True):
    cars = []
    page = requests.get(URL,headers=headers)
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
    try:
        page = requests.get(link, headers=headers)
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
    except Exception as e:
        logger.debug("Error in Scrapping")
        logger.debug(e)
        logger.debug("Error at the following link:")
        logger.debug(link)
        


def setContent(title, link, price, posted, userId, firstSearch):
    formatPosted = datetime.strptime(posted, '%Y-%m-%d  %H:%M')
    auto = Auto(link = link,title = title,price = price,posted = formatPosted,userId = userId)
    if firstSearch == True:
        logger.debug('New auto was saved')
        auto.save()
    return {
     "link":link,
     "title":title,
     "price":price,
     "posted":posted
    }


def generateQuery(parameter: Parameters):
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