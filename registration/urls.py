from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as log_views
from . import views

urlpatterns = [
    path('login/', log_views.login, name='login'),
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
]
