from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import BookingForm, LoginForm, CarbonForm
from .forms import SignupForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def about(request):
    return render(request, 'about.html')



def carboncalc(request):
    if request.method == 'POST':
        form = CarbonForm(request.POST)
        if form.is_valid():
            electricity = form.cleaned_data['electricity']
            natural_gas = form.cleaned_data['natural_gas']
            heating_oil = form.cleaned_data['heating_oil']
            coal = form.cleaned_data['coal']
            lpg = form.cleaned_data['lpg']
            propane =form.cleaned_data['propane']
            wood = form.cleaned_data['wood']

            emission_factors = {
                'electricity': 0.5,
                'natural_gas': 2.2,
                'heating_oil': 2.5,
                'coal': 2.9,
                'lpg': 1.5,
                'propane': 1.6,
                'wood': 0.3,
            }

            total_emissions = (
                electricity * emission_factors['electricity'] +
                natural_gas * emission_factors['natural_gas'] +
                heating_oil * emission_factors['heating_oil'] +
                coal * emission_factors['coal'] +
                lpg * emission_factors['lpg'] +
                propane * emission_factors['propane'] +
                wood * emission_factors['wood']
            )

            messages.success(request, f'Total Carbon Emissions: {total_emissions:.2f} kg CO2')
        else:
            messages.error(request, 'Please correct the errors below.')
    if request.method == 'POST':
        form = CarbonForm(request.POST)
    else:
        form = CarbonForm()

    return render(request, 'carboncalc.html', {'form': form})

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
            messages.success(request, 'Booking request submitted successfully!')
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