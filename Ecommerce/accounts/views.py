from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    template_name = "forms/form.html"
    form_class = UserRegisterationForm
    extra_context = {
        "title" : "Sign Up",
        "submit" : "Sign Up"
    }
    success_url = reverse_lazy("home")