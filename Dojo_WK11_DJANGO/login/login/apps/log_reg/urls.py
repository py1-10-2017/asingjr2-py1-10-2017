from django.conf.urls import url
from . import views
import regex 
import bcrypt

urlpatterns = [
    url(r'$', views.index), 
    url(r'^success$', views.success)
]