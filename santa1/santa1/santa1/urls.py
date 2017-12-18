from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.santa_ver_1.urls', namespace='santa_ver_1'))
]
