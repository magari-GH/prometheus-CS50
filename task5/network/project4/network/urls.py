
from django.urls import path

from . import views

urlpatterns = [
    path("following", views.following, name="following"),
    path("follow", views.follow, name="follow"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("compose", views.compose, name="compose"),
    path("<str:tab>", views.represent, name="represent"),

]
