from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.views.generic import CreateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from backend.mixins import NextUrlMixin, RequestFormAttachMixin, NotAccessMixin
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


class RegisterView(NotAccessMixin, CreateView):
    template_name = 'accounts/register-form.html'
    success_url = '/'
    form_class = RegisterForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegisterView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form_class
        return context



class LoginView(NotAccessMixin, NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login-form.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/user-profile.html'

    def get_object(self, *args, **kwargs):
        queryset = User.objects.filter(slug=self.kwargs.get('slug'))
        if queryset.exists():
            person = queryset.first()
            return person

    def dispatch(self, *args, **kwargs):
        queryset = User.objects.filter(slug=self.kwargs.get('slug'))
        if not queryset.exists():
            return redirect('/')
