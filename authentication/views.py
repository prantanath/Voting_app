from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import user_passes_test


from .forms import UserAuthenticationForm,UserRegisterationForm
#regestering user through admin
@user_passes_test(lambda u: u.is_superuser)
def register_view(request):
    if request.method=="POST":
        form=UserRegisterationForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save() 
            # login(request,user)
            return redirect('admin_dashboard')
        else:
            return render(request,'register.html',{'f':form})
    form=UserRegisterationForm()
    return render(request,'register.html',{'f':form})

def login_view(request):
    if request.method=="POST":
        form=UserAuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=user_name,password=password)
            if user!=None:
                login(request,user)
                if user.is_superuser==True:
                    return redirect('admin_dashboard')
                return redirect('user_dashboard')
        else:
            return render(request,'home.html',{'form':form})
    form=UserAuthenticationForm()
    return render(request,'home.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('/')