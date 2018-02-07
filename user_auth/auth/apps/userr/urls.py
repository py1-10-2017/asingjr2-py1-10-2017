from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path("", views.Index, name="index"), 
    path("register", views.UserFormView.as_view(), name="register"),
    path("main", views.Main, name="main"),
    path("login", login, {"template_name": "userr/registration_form.html"}),

]
