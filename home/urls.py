
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.index),
    path('login/', views.index),



]
