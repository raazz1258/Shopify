
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .form import LoginForm

urlpatterns = [
    path('', views.index, name= 'index'),
    path('register/', views.register, name= 'register'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),



]
