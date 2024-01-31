from datetime import date,timedelta
from django.http import Http404
from django.db.models import Count
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, redirect,get_object_or_404
from .forms import RestaurantForm,MenuForm
from .models import Restaurant,Menu,Vote
from authentication.models import Employee

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'admindashboard.html')  # Redirect to the page displaying all restaurants
    else:
        form = RestaurantForm()

    return render(request, 'create_restaurant.html', {'f': form})

@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    restaurants = Restaurant.objects.all()
    employees = Employee.objects.exclude(username=request.user.username)
    return render(request, 'admindashboard.html', {'restaurants': restaurants,'employees':employees})

@user_passes_test(lambda u: u.is_superuser)
def add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    restaurant_menus = Menu.objects.filter(restaurant=restaurant)

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return redirect('admin-dashboard')
    else:
        form = MenuForm()

    return render(request, 'add_menu.html', {'form': form, 'restaurant': restaurant,'menus':restaurant_menus})

@user_passes_test(lambda u: u.is_superuser)
def delete_menu(request,id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    return redirect('admin_dashboard')

@login_required
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

@user_passes_test(lambda u: u.is_superuser)
def delete_restaurant(request,id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    return redirect('admin_dashboard')

@login_required
def show_results(request):
    try:
        # Getting the date of three days ago
        three_days_ago = date.today() - timedelta(days=2)
        todays_list = Menu.objects.filter(date=date.today()).annotate(vote_count=Count('vote')).order_by('-vote_count')
        winners_list = []
        print(todays_list[0])
        for day in range(2):
            current_day = three_days_ago + timedelta(days=day)
            winner = Menu.objects.filter(date=current_day).annotate(vote_count=Count('vote')).order_by('-vote_count').first()
            if winner is not None:
                winners_list.append(winner)
        if len(winners_list) < 2:
            return render(request, 'show_results.html', {'winner': todays_list[0]})
        for winner in winners_list:
            if winner.restaurant != todays_list[0].restaurant:
                return render(request, 'show_results.html', {'winner': todays_list[0]})
        return render(request, 'show_results.html', {'winner': todays_list[1]})
    except IndexError:
        if todays_list:
            return render(request, 'show_results.html', {'winner': todays_list[0]})
        else:
            raise Http404("No winners found.")    
    
