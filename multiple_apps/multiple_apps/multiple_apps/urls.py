
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^survey/', include('apps.survey.urls', namespace='survey')),
    url(r'^val_log_reg/', include('apps.val_log_reg.urls', namespace='val_log_reg')),
    url(r'^sim_form/', include('apps.sim_form.urls', namespace='sim_form')),
]
