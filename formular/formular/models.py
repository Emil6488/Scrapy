from django.db import models


class FormQuery(models.Model):
    userId = models.IntegerField()
    minPrice = models.IntegerField()
    maxPrice = models.IntegerField()
    minYear = models.IntegerField()
    maxYear = models.IntegerField()
    minOdometer = models.IntegerField()
    maxOdometer = models.IntegerField()
    condition = models.IntegerField()
    miles =  models.IntegerField()
    postalCode =  models.IntegerField()
    carModel = models.CharField(max_length=100)

