from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from accounts.forms import UserRegisterForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            messages.error(request, 'wrong credentials' )
            return redirect('accounts:login_page')
        
    return render(request,"accounts/login.html")

''' register view'''
def register_page(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.username = 'test'
            user.save()
            return redirect('accounts:login_page')
        print(form.errors,"----------")
    else:
        form = UserRegisterForm()       
    context = {
        'form': form,   
    }        
    return render(request, 'accounts/register.html', context)

'''logout view''' 
@login_required(login_url='/')
def logout_process(request):
    logout(request)
    return redirect('accounts:login_page')
    