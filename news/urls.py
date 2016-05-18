from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/dlt/$', views.post_dlt, name='post_dlt'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.comment_new, name='comment_new'),
    url(r'^post/(?P<pk>[0-9]+)/comment/(?P<id>[0-9]+)/dlt/$', views.comment_dlt, name='comment_dlt'),
]