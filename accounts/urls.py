from django.conf.urls import url
from django.contrib.auth.views import login
from . import views



urlpatterns =[
    url(r'^register/$', views.register, name ="register" ),
    url(r'^login/$', views.Mylogin, name = 'login'),
]