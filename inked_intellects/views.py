from django.shortcuts import render
from .models import Inked
# Create your views here.
from django.views.generic import ListView, DetailView



class InkedListView(ListView):
    model = Inked
    template_name = "inked_intellects/inked_intellects_list.html"
    ordering = ['-created_at']


class InkedDetailView(DetailView):
    model = Inked
    template_name = "inked_intellects/inked_intellects_detail.html"


