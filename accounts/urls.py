from django.conf.urls import url
from django.contrib.auth.views import login
from . import views



urlpatterns =[
    url(r'^register/$', views.register, name ="register" ),
    url(r'^login/$', login, name = 'login', kwargs={'template_name':'accounts/login.html'}),
]