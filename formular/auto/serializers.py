from rest_framework import serializers 
from auto.models import Auto
 
 
class AutoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Auto
        fields = ('id',
                  'link',
                  'title',
                  'price',
                  'posted')