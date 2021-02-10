from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-landing"),
    path('about/', views.about, name="home-about"),
    path('assets/logo/Thumbnail.png',views.repo, name="assets"),
]
