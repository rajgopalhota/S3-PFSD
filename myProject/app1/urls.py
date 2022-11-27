from django.contrib import admin
from django.urls import path, include
from . import  views
urlpatterns = [
    path('', views.Hello, name = 'Hello'),
    path('login/', views.Login, name = 'login'),
]
