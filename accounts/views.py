from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from accounts.forms import UserRegisterForm 

'''
login view
'''
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page') 
    #post method for login    
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, email=email, password=password) #authenticating user
        if user is not None:
            login(request=request, user=user)
            return redirect('dashboard:dashboard_page')
        else:
            return redirect('accounts:login_page')
        
    return render(request,"accounts/login.html")

''' register view'''
def register_page(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_page')
        else:
            form = UserRegisterForm()
        context = {
            "form":form
        }
        
    return render(request,"accounts/register.html", context)
