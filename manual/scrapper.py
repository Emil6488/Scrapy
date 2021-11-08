import requests
from bs4 import BeautifulSoup
from helper import checkDates, findLatest


def scrapDateAndQuery(latestCar,query,exists):
    cars = []
    URL = "https://losangeles.craigslist.org/d/cars-trucks-by-owner/search/cto"
    if exists is True:
        URL = "https://losangeles.craigslist.org/d/cars-trucks-by-owner/search/cto"+query
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    searchResults = soup.find(id="search-results")
    carRows = searchResults.find_all("li", class_="result-row")
    counter = 0
    for car in carRows:
        url = car.find("a", href=True)
        priceClass = url.find("span", class_="result-price")
        price = 0
        if priceClass is None:
            price = 0
        else: 
            price = priceClass.text
        link = url['href']
        carIn = requests.get(url['href'])
        soupIn = BeautifulSoup(carIn.content, "html.parser")
        #extract posted
        dateBar = soupIn.find("header", class_="dateReplyBar")
        time = dateBar.find("time", class_="date")
        posted = time.text.strip()
        print("Date 1="+latestCar)
        print("Date 2="+posted)
        print(findLatest(latestCar, posted))
        if findLatest(latestCar, posted) is False:
            attr = soupIn.find("div", class_="mapAndAttrs")
            name = attr.find("p", class_="attrgroup")
            title = name.text.strip()
            cars.append(setContent(title,link,price,posted))
        else:
            return cars






def scrapMain(limit, URL = "https://losangeles.craigslist.org/d/cars-trucks-by-owner/search/cto"):
    cars = []   
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    searchResults = soup.find(id="search-results")
    carRows = searchResults.find_all("li", class_="result-row")
    counter = 0
    for car in carRows:
        url = car.find("a", href=True)
        price = url.find("span", class_="result-price")
        if price is None:
            parsedCar = scrapContent(url['href'],0)
        else:
            parsedCar = scrapContent(url['href'],price.text)        
        cars.append(parsedCar)
        limit = limit - 1
        if limit == 0:
            return cars

def scrapContent(link,price):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    #extract posted
    dateBar = soup.find("header", class_="dateReplyBar")
    time = dateBar.find("time", class_="date")
    posted = time.text.strip()
    #extract name
    attr = soup.find("div", class_="mapAndAttrs")
    name = attr.find("p", class_="attrgroup")
    title = name.text.strip()
    return setContent(title,link,price,posted)


def setContent(title,link,price,posted):
    return {
        "link":link,
        "title":title,
        "price":price,
        "posted":posted
    }