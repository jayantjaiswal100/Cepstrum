from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.
class HomeView(ListView):
    """docstring for ThanksPage."""
    model = Talk
    template_name = 'talk/home.html'
