from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserRegistrationForm, CustomUserLoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'cars/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'cars/login.html', {'form': form})


def home(request):
    return render(request, 'home.html')