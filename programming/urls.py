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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from pokemon import views as pokemon_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),
    url(r'^about/', views.about),
    url(r'^gallery/',views.gallery),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$',views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$',views.mysum),
    url(r'^sum/(?P<x>\d+)/$',views.mysum),
    url(r'^sum2/(?P<x>[\d/]+)/$', views.mysum2),
    url(r'^pokemon_main/$', pokemon_views.pokemon_main),
    url(r'^pokemon/$', pokemon_views.pokemon_list),
    url(r'^pokemon/(?P<pk>\d+)/$', pokemon_views.pokemon_detail),
    url(r'^player/$', pokemon_views.player_list),
    url(r'^player/(?P<pk>\d+)/$', pokemon_views.player_detail),
    url(r'^capture/$', pokemon_views.capture_list),
    url(r'^capture/(?P<pk>\d+)/$', pokemon_views.capture_detail),
    url(r'^place/$', pokemon_views.place_list),
    url(r'^place/(?P<pk>\d+)/$', pokemon_views.place_detail),


]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, docuument_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, docuument_root=settings.MEDIA_ROOT)

