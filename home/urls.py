from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('cdc', views.cdc, name='cdc'),
    path('login', views.loginPage, name ="login"),
    path('signup', views.registerPage , name ="signup"),
    path('logout', views.logoutUser , name ="logout"),
    path('user', views.DataAdder, name='user'),
    path('edit', views.DataEditor, name='edit'),
    path('viewer', views.DataFilter, name='filter'),

    ####
    # path('viewer', views.DataViewer, name='viewer'),
    
    
]