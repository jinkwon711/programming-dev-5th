from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list ,name = 'post_list'),
    url(r'^post/(?P<pk>\d+)/$' ,views.post_detail, name = 'post_detail'),
    url(r'^post/$', views.post_new , name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$' ,views.post_edit, name = 'post_edit'),

    url(r'^post/(?P<post_pk>\d+)/comment/$', views.comment_new, name ='comment_new'),
    url(r'^post/(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$',views.comment_edit, name='comment_edit'),

    url(r'^about/', views.about),
    url(r'^gallery/',views.gallery),

    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$',views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$',views.mysum),
    url(r'^sum/(?P<x>\d+)/$',views.mysum),
    url(r'^sum2/(?P<x>[\d/]+)/$', views.mysum2),

    url(r'^zipcode/$', views.zipcode, name = 'zipcode'),


    ]