import time
from parameters.models import Parameters

def generateURL(param: Parameters):
    mainURL = ""
    if param.area == 'losangeles':
        mainURL = "https://losangeles.craigslist.org/search<subArea>/cta?"
    else:
        mainURL = "https://sfbay.craigslist.org/search<subArea>/cta?"
    #los angeles
    if param.subArea == '1':
        mainURL.replace("<subArea>", "/")
    elif param.subArea == 'sfv':
        mainURL.replace("<subArea>", "/sfv")
    elif param.subArea == 'ant':
        mainURL.replace("<subArea>", "/ant")
    elif param.subArea == 'lac':
        mainURL.replace("<subArea>", "/lac")
    elif param.subArea == 'lgb':
        mainURL.replace("<subArea>", "/lgb")
    elif param.subArea == 'sgv':
        mainURL.replace("<subArea>", "/sgv")
    elif param.subArea == 'wst':
        mainURL.replace("<subArea>", "/wst")
    #san francisco
    elif param.subArea == 'eby':
        mainURL.replace("<subArea>", "/eby")
    elif param.subArea == 'nby':
        mainURL.replace("<subArea>", "/nby")
    elif param.subArea == 'pen':
        mainURL.replace("<subArea>", "/pen")
    elif param.subArea == 'sfc':
        mainURL.replace("<subArea>", "/sfc")
    elif param.subArea == 'scz':
        mainURL.replace("<subArea>", "/scz")
    else:
        mainURL.replace("<subArea>", "/sby")
    return mainURL
    