from django.http import response
from django.shortcuts import render

from django.http.response import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from . import functions
from auto.serializers import AutoSerializer
from auto.models import Auto
from parameters.models import Parameters

@api_view(['GET'])
def startQuery(request,pk):    
    try: 
        parameter = Parameters.objects.get(userId=pk)
        parameter.active = True
        parameter.save() 
    except Parameters.DoesNotExist: 
        param = Parameters(userId = pk,active = True)
        param.save()
    autos = functions.scrapMain(5,pk)
    for auto in autos:
        print(auto)
    return JsonResponse(autos, status=status.HTTP_200_OK, safe=False) 

@api_view(['GET'])
def endQuery(request,pk):
    try: 
        parameter = Parameters.objects.get(userId=pk) 
        parameter.active = False
        parameter.save()
    except Parameters.DoesNotExist: 
        return JsonResponse({'message': 'The parameters does not exist'}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'message': 'Confirmed'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def scrapLoop(request,pk):
    try: 
        parameter = Parameters.objects.get(userId=pk, active=True)
    except Parameters.DoesNotExist: 
        return JsonResponse({'message': 'The parameters does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if parameter.active == False:
        return JsonResponse({'message': 'Activate start'}, status=status.HTTP_403_FORBIDDEN)
    url = "https://losangeles.craigslist.org/d/cars-trucks/search/cta?"
    query = functions.generateQuery(parameter)
    print(url+query)
    autos = functions.scrapMain(5, pk,url+query,False)
    responseAutos = []
    for auto in autos:
        print(auto["link"])
        try: 
            newAuto = Auto.objects.get(link=auto["link"], userId=pk)
        except Auto.DoesNotExist:
            freshAuto = Auto(link = auto["link"],title = auto["title"],price = auto["price"],posted = auto["posted"],userId=pk)
            freshAuto.save()
            responseAutos.append(auto)
    if len(responseAutos)> 0:
        return JsonResponse(responseAutos, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'message': 'No new autos'}, status=status.HTTP_404_NOT_FOUND)





     
