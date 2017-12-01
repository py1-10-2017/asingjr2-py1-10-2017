from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.val_log_reg.urls'))
]
