from django.conf.urls import url 
from . import views 


urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^post$', views.post),
    url(r'^add$', views.add),
    url(r'^show_add$', views.show_add),
    url(r'^test$', views.test), 
    url(r'^user_activity$', views.user_activity)
]
