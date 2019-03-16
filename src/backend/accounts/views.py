from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.views.generic import CreateView, FormView
from backend.mixins import NextUrlMixin, RequestFormAttachMixin, NotAccessMixin
# Create your views here.


class RegisterView(NotAccessMixin, CreateView):
    template_name = 'accounts/register-form.html'
    success_url = '/'
    form_class = RegisterForm


class LoginView(NotAccessMixin, NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login-form.html'
