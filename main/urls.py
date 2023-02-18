
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home' ),
    path('search',views.search, name = 'search' ),
    path('car_sale/', views.add_newcar, name='car_sale'),
    path('new_auto_part/', views.new_auto_part, name='new_auto_part'),
    path('new_service/', views.new_service, name='new_service'),
    path('edit_car/<str:pk>/', views.update_car, name = 'update_car'),
    path('delete_car/<str:pk>/', views.delete_car, name = 'delete_car'),
    path('see_details/<str:pk>/', views.see_details, name = 'details'),
    path('fav/<str:id>/', views.add_tofavourite, name = 'to_favourite'),
    path('fav/', views.favourite_list, name = 'favourite_list'),
    path('Login/', views.loginPage, name = 'login'),
    path('ErrorPage/', views.ErrorPage, name = 'error'),
    path('Logout/', views.logoutUser, name = 'logout'),
    path('Register/', views.registerPage, name = 'register'),
    path('welcome/', views.greetingPage, name = 'greeting')
]