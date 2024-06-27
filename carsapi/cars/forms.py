from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from cars.models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'password1', 'password2']

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']