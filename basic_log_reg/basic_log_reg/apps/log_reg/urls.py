from django.conf.urls import url
from . import views
from .models import *
import Bcrypt
import re

urlpatterns = [
    url(r'index$', views.index), 
    url(r'^post$', views.post),
    url(r'success$', views.success)
]