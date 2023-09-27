from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('index', views.index , name = 'index'),
    path('about', views.about, name = 'about'),
    path('career', views.career, name = 'career'),
    path('contact', views.contact, name = 'contact'),
    path('apply/', views.apply, name = 'apply'),
    path('require/', views.require, name = 'require'),
    
    
    
   
]
