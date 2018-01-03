from django.conf.urls import url  
from . import views 

app_name='wish'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'^new$', views.new, name='new'),
    url(r'^main$', views.main, name='main'),
    url(r'^(?P<item_id>\d+)/item$', views.item, name='item'),
    url(r'^logout$', views.logout, name='logout'),
]
