from django.shortcuts import render

from django.http.response import HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from . import functions
from auto.serializers import AutoSerializer

@api_view(['GET'])
def addAutos(request):
    autos = functions.scrapMain(5)     
    return HttpResponse("Completed", status=status.HTTP_200_OK) 
