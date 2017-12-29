from django.conf. urls import url 
from . import views 

app_name= 'forms'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^$', views.index2, name='index2'),
    url(r'^post$', views.post, name='post'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^display$', views.display, name='display'),
]