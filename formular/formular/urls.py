from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('parameters.urls')),
    url(r'^', include('auto.urls')),
]

urlpatterns += staticfiles_urlpatterns()