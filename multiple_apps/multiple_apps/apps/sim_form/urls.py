from django.conf.urls import url
from . import views

app_name='sim_form'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'), 
    url(r'^display$', views.display, name='display')
]