from django.db import models

# Create your models here.
class Parameters(models.Model):
    userId = models.IntegerField(null=True)
    minPrice = models.IntegerField(null=True)
    maxPrice = models.IntegerField(null=True)
    minYear = models.IntegerField(null=True)
    maxYear = models.IntegerField(null=True)
    minOdometer = models.IntegerField(null=True)
    maxOdometer = models.IntegerField(null=True)
    condition = models.IntegerField(null=True)
    miles =  models.IntegerField(null=True)
    postalCode =  models.IntegerField(null=True)
    carModel = models.CharField(max_length=100, null=True)
