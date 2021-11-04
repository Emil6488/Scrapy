from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    url(r'^api/auto/start/(?P<pk>[0-9]+)$$', views.startQuery),
    url(r'^api/auto/end/(?P<pk>[0-9]+)$$', views.endQuery),
    url(r'^api/scrap/(?P<pk>[0-9]+)$$', views.scrapLoop),
]