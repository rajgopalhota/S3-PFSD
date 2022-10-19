from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.LoginView, name = 'login'),
    path('register/', views.Register, name = 'register'),
    path('ridenow/', views.Ridenow, name = 'ridenow'),
    path('schedule/', views.Ridelater, name = 'schedule'),
    path('home/', views.Home, name = 'home'),
]
