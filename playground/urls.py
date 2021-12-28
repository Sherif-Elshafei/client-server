from django.urls import path
from . import views

urlpatterns = [
    path ('hello/', views.say_hello),
    path ('hello_friend', views.say_hello_friend)
    ]	