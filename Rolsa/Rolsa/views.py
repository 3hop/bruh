from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BookingForm, LoginForm
from .forms import SignupForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'index.html')


def book(request):
    return render(request, 'book.html')

def about(request):
    return render(request, 'about.html')

def consultations(request):
    return render(request, 'consultations.html')



def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            return
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')