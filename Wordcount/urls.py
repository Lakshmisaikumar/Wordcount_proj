from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('input/', views.homepage, name = 'homepage'),
    path('count/', views.count, name = 'count' ),
    path('about/', views.about, name = 'about'),
]
