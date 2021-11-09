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
    except Parameters.DoesNotExist: 
        param = Parameters(userId = pk,active = True)
        param.save()
        autos = functions.scrapMain(5,pk)
        return JsonResponse(autos, status=status.HTTP_200_OK, safe=False)
    if parameter.active == False:
        parameter.active = True
        parameter.save()
        autos = functions.scrapMain(5,pk)
        for auto in autos:
            return JsonResponse(autos, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=status.HTTP_403_FORBIDDEN)
    

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
def scrapLoop(request):
    parameters = Parameters.objects.filter(active=True)
    allResponses = {}
    for parameter in parameters:
        if parameter.active == False:
            allResponses['user'+str(parameter.userId)].append('Activate start')
            continue
            #return JsonResponse({'message': 'Activate start'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        url = "https://losangeles.craigslist.org/d/cars-trucks/search/cta?"
        query = functions.generateQuery(parameter)
        autos = functions.scrapMain(15, parameter.userId,url+query,False)
        print(url+query)
        responseAutos = []
        for auto in autos:            
            try: 
                newAuto = Auto.objects.get(link=auto["link"], userId=parameter.userId)
            except Auto.DoesNotExist:
                freshAuto = Auto(link = auto["link"],title = auto["title"],price = auto["price"],posted = auto["posted"],userId=parameter.userId)
                freshAuto.save()
                responseAutos.append(auto)        
        if len(responseAutos) == 0:
            allResponses[str(parameter.userId)] = 'No new autos'
        else:
            allResponses[str(parameter.userId)] = responseAutos
    return JsonResponse(allResponses, status=status.HTTP_200_OK, safe=False)





     
