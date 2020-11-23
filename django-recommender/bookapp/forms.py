from .models import *
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1']   

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'price', 'image_link']
    