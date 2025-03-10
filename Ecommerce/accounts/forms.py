from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","image")