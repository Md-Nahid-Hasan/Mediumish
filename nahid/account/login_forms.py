from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms.widgets import Widget
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(forms.Form):
    
    
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter username'
            }), 
            required=True
        )

    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter password'
            }), 
            required=True
        )
    

        
        
        
