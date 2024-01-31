
from django.contrib import admin
from django.urls import path,include
from .views import *
from restaurant_lunch_vote.views import admin_dashboard,user_dashboard
urlpatterns = [
     path('', login_view, name='login'),
     path('register',register_view,name="register"),
     path('logout',user_logout,name="logout"),
     path('admin_dashboard',admin_dashboard,name="admin_dashboard"),
     path('user_dashboard',user_dashboard,name="user_dashboard"),
]
