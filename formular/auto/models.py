from django.db import models

class Auto(models.Model):
    userId = models.PositiveBigIntegerField(null=True)
    link = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200,blank=False, default='')
    price = models.CharField(max_length=200, default= 0)
    posted = models.DateTimeField(null=True)

    def __repr__(self):
        return "{"+"link:"+self.link+","+"title:"+self.title+","+"price"+self.price+","+"posted"+self.posted+"}"
