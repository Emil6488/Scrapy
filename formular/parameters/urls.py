from django.conf.urls import url 
from parameters import views 
 
urlpatterns = [ 
    url(r'^api/parameters$', views.postForm),
    url(r'^api/parameters/(?P<pk>[0-9]+)$', views.getFormbyId),
]