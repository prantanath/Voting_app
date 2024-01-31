from datetime import date
from django.shortcuts import render, redirect,get_object_or_404
from .forms import RestaurantForm,MenuForm
from .models import Restaurant,Menu
# Create your views here.

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'admindashboard.html')  # Redirect to the page displaying all restaurants
    else:
        form = RestaurantForm()

    return render(request, 'create_restaurant.html', {'f': form})

def admin_dashboard(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'admindashboard.html', {'restaurants': restaurants})

def add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return render(request,'admindashboard.html')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form, 'restaurant': restaurant})

def user_dashboard(request):
    current_day_menus = Menu.objects.filter(date=date.today())
    return render(request, 'employee_dashboard.html', {'menus': current_day_menus})
