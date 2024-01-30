
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
     path('', login_view, name='login'),
     path('register',register_view,name="register"),
     path('logout',user_logout,name="logout"),
]
