from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from parameters.models import Parameters
from parameters.serializers import ParametersSerializer
from rest_framework.decorators import api_view

from django.http.response import HttpResponse
from rest_framework import status

from parameters.models import Parameters
from . import forms

endpoint = "https://0a19-131-220-35-155.ngrok.io"

# Create your views here.
@api_view(['POST'])
def postForm(request):
    formData = request.POST.dict()
    minPrice = int(formData.get("minPrice"))
    maxPrice = int(formData.get("maxPrice"))
    minYear = int(formData.get("minYear"))
    maxYear = int(formData.get("maxYear"))
    minOdometer = int(formData.get("minOdometer"))
    maxOdometer = int(formData.get("maxOdometer"))
    condition = int(formData.get("condition"))
    miles = int(formData.get("miles"))
    postalCode = int(formData.get("postalCode"))
    carModel = formData.get("carModel")
    newParam = Parameters(
        minPrice=minPrice,
        maxPrice=maxPrice,
        minYear=minYear,
        maxYear=maxYear,
        minOdometer=minOdometer,
        maxOdometer=maxOdometer,
        condition=condition,
        miles=miles,
        postalCode=postalCode,
        carModel=carModel,
    )
    newParam.save()
    return HttpResponse("Filter Updated", status=status.HTTP_200_OK)



@api_view(['GET'])
def getParameterValues(request,pk):
    try: 
        parameter = Parameters.objects.get(userId=pk) 
    except Parameters.DoesNotExist: 
        return JsonResponse({'message': 'The parameters does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    parameterSerialize = ParametersSerializer(parameter) 
    return JsonResponse(parameterSerialize.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getFormLink(request,pk):
    try: 
        parameter = Parameters.objects.get(userId=pk)
        return JsonResponse({'message': endpoint + '/api/form'}, status=status.HTTP_200_OK) 
    except Parameters.DoesNotExist: 
        return JsonResponse({'message': 'The parameters does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
@api_view(['GET'])
def formDef(request):
    return render(request, 'form.html')
