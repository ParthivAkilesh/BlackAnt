from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name ="login"),
    path('signup', views.registerPage , name ="signup"),
    path('logout', views.logoutUser , name ="logout"),
    path('admin_page', views.admin_page , name ="admin_page"),
    path('addData', views.DataAdder, name='addData'),
    path('success', views.DataAdded, name='success'),
    path('viewer', views.DataViewer, name='viewer'),
    
    
]