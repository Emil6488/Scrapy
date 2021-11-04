from django.conf.urls import url 
from auto  import views 

urlpatterns = [ 
    url(r'^api/auto$', views.addAutos),
]