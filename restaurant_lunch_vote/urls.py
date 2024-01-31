from django.urls import path,include
from .views import admin_dashboard, add_menu,create_restaurant,vote,delete_restaurant

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin-dashboard'),
    path('add-menu/<int:restaurant_id>/', add_menu, name='add_menu'),
    path('create-restaurant',create_restaurant,name="create-restaurant"),
    path('vote',vote,name="vote"),
    path('delete-restaurant/<id>',delete_restaurant,name="delete-restaurant")
]
