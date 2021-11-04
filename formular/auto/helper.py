import time

def checkDates(date1,date2):
    if date1 is None:
        return date2
    if date2 is None:
        return date1
    formatted_date1 = time.strptime(date1, "%Y-%m-%d %H:%M")
    formatted_date2 = time.strptime(date2,  "%Y-%m-%d %H:%M")
    if formatted_date1 > formatted_date2:
        return date1
    else:
        return date2

def findLatest(latestCar,newCar):
    if latestCar is None:
        return newCar
    if newCar is None:
        return latestCar
    formattedDate1 = time.strptime(latestCar, "%Y-%m-%d %H:%M")
    formatNewCar = time.strptime(newCar,  "%Y-%m-%d %H:%M")
    if formattedDate1 == formatNewCar:
        return True
    if formattedDate1 < formatNewCar:
        return False
    