from django.conf.urls import url
from . import views

app_name = 'santa_ver_1'
urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^reg$', views.reg, name='reg'),
    url(r'^log$', views.log, name='log'),
    url(r'^main$', views.main, name='main'),
    url(r'^post$', views.post, name='post'),
    url(r'^enter_members$', views.enter_members, name = 'enter_members'),
    url(r'^(?P<ml_id>\d+)/add_member$', views.add_member, name='add_member'),
    url(r'^(?P<list_id>\d+)/list_update$', views.list_update, name='list_update'),
    url(r'^(?P<list_id>\d+)/list_delete$', views.list_delete, name='list_delete'),
    url(r'^(?P<list_id>\d+)/view_members$', views.view_members, name='view_members'),
    url(r'^logout$', views.logout, name='logout')         
]
