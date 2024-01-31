from datetime import date
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import RestaurantForm,MenuForm
from .models import Restaurant,Menu,Vote
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
            return redirect('admin-dashboard')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form, 'restaurant': restaurant})

def user_dashboard(request):
    current_day_menus = Menu.objects.filter(date=date.today()).annotate(vote_count=Count('vote')).order_by('-vote_count')
    return render(request, 'employee_dashboard.html', {'menus': current_day_menus})

@login_required
def vote(request):
    if request.method == 'POST':
        menu_id = request.POST.get('menu_id')
        menu = Menu.objects.get(pk=menu_id)

        # Checking if the user has already voted for a menu today
        existing_vote = Vote.objects.filter(employee=request.user, menu__date=date.today())
        if existing_vote.exists():
            return redirect('/')

        Vote.objects.create(employee=request.user, menu=menu)
        return redirect('user_dashboard')

    return redirect('/')

def delete_restaurant(request,id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    return redirect('admin_dashboard')