from django.conf.urls import url
from . import views

app_name='val_log_reg'
urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'success$', views.success, name='success')
]
