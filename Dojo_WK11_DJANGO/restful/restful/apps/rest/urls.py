'''
Need 7 routes
GET index to show all
GET show to display individual user
GET new to create new with form
GET update to update existing 
GET to delete
POST to capture and send new
POST to capture and send updates
'''

from django.conf.urls import url
from .models import *
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),  #will post to separate view
    url(r'^post_new$', views.post_new), #NO SLASHES NEED IN BEGINNING!!!!!!!
    url(r'^(?P<user_id>\d+)/display$', views.display),  #add later instead of below 
    url(r'^(?P<user_id>\d+)/update$', views.update),      #add later instead of below
    url(r'^(?P<user_id>\d+)/post_update$', views.post_update),
    url(r'^(?P<user_id>\d+)/delete$', views.delete)
]


'''
Must use url params to update form using database information, delete information, or display
Must match exising template information and index view information
'''