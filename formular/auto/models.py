from django.db import models

class Auto(models.Model):
    link = models.IntegerField(null=True)
    title = models.CharField(max_length=200,blank=False, default='')
    price = models.IntegerField(max_length=200, default= 0)
    posted = models.DateTimeField()
