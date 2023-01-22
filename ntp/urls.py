from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('home/',views.home,name="home"),
    path('login/',views.jamun,name="login"),
    path('userregistered/',views.login,name="userregistered"),
    path('register/',views.register,name="register"),
    path('registering/',views.registering,name="done"),
    path('mess/',views.mess,name="mess"),
    path('user/',views.gobackuser,name="user"),
    path('applymess/',views.applymess,name="applymess"),
    path('bookroom/',views.bookroom,name="bookroom"),
    path('booked/',views.booked,name="booked"),
    path('confirmbooking/',views.confirmbooking,name="confirmbooking"),
    path("mydetails/",views.mydetails,name="mydetails")
]
