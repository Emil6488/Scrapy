import time
from parameters.models import Parameters

def locationBasedURL(param: Parameters):
    mainURL = ""
    if param.area == 'losangeles':
        mainURL = "https://losangeles.craigslist.org/search"
    else:
        mainURL = "https://sfbay.craigslist.org/search"
    if param.subArea == '1':
        mainURL = mainURL+'/cta?'
    elif param.subArea == 'sfv':
        mainURL = mainURL+'/sfv/cta?'
    elif param.subArea == 'ant':
        mainURL = mainURL+'/ant/cta?'
    elif param.subArea == 'lac':
        mainURL = mainURL+'/lac/cta?'
    elif param.subArea == 'lgb':
        mainURL = mainURL+'/lgb/cta?'
    elif param.subArea == 'sgv':
        mainURL = mainURL+'/sgv/cta?'
    elif param.subArea == 'wst':
        mainURL = mainURL+'/wst/cta?'
    #san francisco
    elif param.subArea == 'eby':
        mainURL = mainURL+'/eby/cta?'
    elif param.subArea == 'nby':
        mainURL = mainURL+'/nby/cta?'
    elif param.subArea == 'pen':
        mainURL = mainURL+'/pen/cta?'
    elif param.subArea == 'sfc':
        mainURL = mainURL+'/sfc/cta?'
    elif param.subArea == 'scz':
        mainURL = mainURL+'/scz/cta?'
    else:
        mainURL = mainURL+'/sby/cta?'
    return mainURL
    