from rest_framework import serializers 
from parameters.models import Parameters
 
 
class ParametersSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Parameters
        fields = ('id','userId','minPrice',	'maxPrice','minYear','maxYear','minOdometer','maxOdometer','condition','miles','postalCode','carModel')