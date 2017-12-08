from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^main$', views.main), 
    url(r'^logout$', views.logout),
    url(r'post$', views.post),
    url(r'^play$', views.play),
    url(r'^play2$', views.play2),
    url(r'^enter_members$', views.enter_members)
    
]
