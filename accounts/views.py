from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from accounts import forms,models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
# Create your views here.
class SignUp(CreateView):
    """docstring for SignUp."""
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class EmailUpdateView(LoginRequiredMixin,UpdateView):
     model = User
     fields = ['email']
     success_url = reverse_lazy('bios:all')
     
