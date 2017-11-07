from django.conf.urls import url
from . import views           # Importing views folder to be able to perform methods

urlpatterns = [
    # For this regex match go to views and do index method
    url(r'^$', views.index) 
]
