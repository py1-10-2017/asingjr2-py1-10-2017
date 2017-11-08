from django.conf.urls import url
from . import views

urlpatterns = [
    # For this regex match go to views and do index method
    url(r'^$', views.index),
    url(r'result$', views.result),
    url(r'survey/process$', views.submit),
    url(r'test$', views.test)
]
