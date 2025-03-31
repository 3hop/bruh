from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Booking

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    enquiry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'How can we help you?'}))
    product = forms.ChoiceField(
        choices=[
            ('solar_panel', 'Solar Panel'),
            ('heat_pump', 'Heat Pump'),
            ('solar_farm', 'Solar Farm'),
            ('home_energy_solutions', 'Home Energy Solutions'),
            ('windmill', 'Windmill'),
            ('electric_charging_system', 'Electric Charging System')
        ],
        widget=forms.Select(attrs={'placeholder': 'Select a Product'})
    )

    def save(self, user, commit=True):
        booking = Booking(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            enquiry=self.cleaned_data['enquiry'],
            product=self.cleaned_data['product'],
        )
        if commit:
            booking.save()
        return booking
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        return user
    
class CarbonForm(forms.Form):
    electricity = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Electricity (kWh)'}))
    natural_gas = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Natural Gas (therms)'}))
    heating_oil = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Heating Oil (gallons)'}))
    coal = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Coal (tons)'}))
    lpg = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'LPG (gallons)'}))
    propane = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Propane (gallons)'}))
    wood = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Wood (cords)'}))
