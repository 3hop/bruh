from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    enquiry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'How can we help you?'}))


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        return user