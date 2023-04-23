from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
from allauth.account.forms import SignupForm


class CustomUserCreationForm(SignupForm):
    class Meta:
        model = User
        fields = (
            
            "email",
            
        )



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            
            "email",
            
        )

