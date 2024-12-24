from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages, auth
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('App_Login:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'App_Login/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth_login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('App_Login:dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'App_login/login.html', {'form': form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('App_Login:login')

@login_required
def dashboard(request):
    return render(request, 'App_Login/dashboard.html', context={})