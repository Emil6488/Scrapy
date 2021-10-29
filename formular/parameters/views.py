from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from parameters.models import Parameters
from parameters.serializers import ParametersSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def postForm(request):
    parameters_data = JSONParser().parse(request)
    print(request)
    parameters_serializer = ParametersSerializer(data=parameters_data)
    if parameters_serializer.is_valid():
        parameters_serializer.save()
        return JsonResponse(parameters_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(parameters_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getFormbyId(request,pk):
    try: 
        parameter = Parameters.objects.get(userId=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The parameters does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    parameterSerialize = ParametersSerializer(parameter) 
    return JsonResponse(parameterSerialize.data)
