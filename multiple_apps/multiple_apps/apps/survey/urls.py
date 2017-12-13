from django.conf.urls import url
from . import views

app_name='survey'
urlpatterns = [
    # For this regex match go to views and do index method
    url(r'^$', views.index, name='index'),
    url(r'result$', views.result, name='result'),
    url(r'survey/process$', views.submit, name='process'),
    url(r'test$', views.test, name='test')
]
