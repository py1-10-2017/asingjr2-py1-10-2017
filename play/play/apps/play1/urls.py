from django.conf.urls import url
from views import generic
from . import views


# app_name = 'play1' 
urlpatterns = [
    url(r'^$', views.index, name= 'index'), 
    url(r'^form$', views.form, name= 'form'), 
    url(r'^test$', views.test, name= 'test'), 
    url(r'^post$', views.post, name= 'post'), 
    #note the change in url param format
    url(r'^(?P<param>\d+)$', views.param_test, name='param_test'),
    url(r'^generic$', generic.as_view(), name='generic'),
    url(r'^logout$', views.logout, name= 'logout'), 
]
 