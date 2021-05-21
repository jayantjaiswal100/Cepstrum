from django.shortcuts import render
from .models import Inphase
# Create your views here.
from django.views.generic import ListView



class InphaseListView(ListView):
    model = Inphase
    template_name = "inphase/inphase_list.html"
    ordering = ['-created_at']

