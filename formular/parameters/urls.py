from django.conf.urls import url 
from parameters import views 
 
urlpatterns = [ 
    url(r'^api/parameters$', views.postForm),
    url(r'^api/form$', views.formDef),
    url(r'^api/form/(?P<pk>[0-9]+)$', views.getFormLink),
    url(r'^api/parameters/(?P<pk>[0-9]+)$', views.getParameterValues),
]