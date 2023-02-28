from django.urls import path, include
from carapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register.html'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('home/',views.home,name='home'),
    path('testdrive/',views.testdrive,name='testdrive'),
    path('cars/',views.Cars,name='cars'),
    path('singleCar/<int:id>',views.singleCar,name="singleCar"),

]