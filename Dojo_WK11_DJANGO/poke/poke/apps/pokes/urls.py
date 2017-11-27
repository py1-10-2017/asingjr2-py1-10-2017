from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post$', views.post),
    url(r'^home$', views.home),
    url(r'^poke_post$', views.poke_post), 
    url(r'^logout$', views.logout)
]