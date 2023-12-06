from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from user.forms import UserSignUpForm
from django.contrib.auth import get_user_model


user = get_user_model()


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


class SignUpView(CreateView):
    model = user
    form_class = UserSignUpForm
    template_name = "register.html"
    success_url = reverse_lazy("post:postlist")
