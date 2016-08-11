"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from pokemon import views as pokemon_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda request: redirect('/blog/')),
    # blog
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # login
    url(r'^accounts/', include('accounts.urls')),

    # pokemon
    url(r'^pokemon_main/$', pokemon_views.pokemon_main),
    url(r'^pokemon/$', pokemon_views.pokemon_list),
    url(r'^pokemon/(?P<pk>\d+)/$', pokemon_views.pokemon_detail),
    url(r'^player/$', pokemon_views.player_list),
    url(r'^player/(?P<pk>\d+)/$', pokemon_views.player_detail),
    url(r'^capture/$', pokemon_views.capture_list),
    url(r'^capture/(?P<pk>\d+)/$', pokemon_views.capture_detail),
    url(r'^place/$', pokemon_views.place_list),
    url(r'^place/(?P<pk>\d+)/$', pokemon_views.place_detail),


    # url(r'^zipcode_exist/$', views.zipcode_exist, name= 'zipcodecheck'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

