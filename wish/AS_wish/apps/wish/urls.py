from django.conf.urls import url  
from . import views 

app_name='wish'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'^new$', views.new, name='new'),
    url(r'^main$', views.main, name='main'),
    url(r'^(?P<item_id>\d+)/item$', views.item, name='item'),
    url(r'^(?P<item_id>\d+)/add_to_wish$', views.add_to_wish, name='add_to_wish'),
    url(r'^(?P<item_id>\d+)/del_from_wish$',
        views.del_from_wish, name='del_from_wish'),
    url(r'^(?P<item_id>\d+)/rem_from_wish$',
        views.rem_from_wish, name='rem_from_wish'),
    url(r'^logout$', views.logout, name='logout'),
]
