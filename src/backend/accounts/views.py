from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
# Create your views here.


class RegisterView(CreateView):
    template_name = 'accounts/register-form.html'
    success_url = '/'
    form_class = RegisterForm
