from django.shortcuts import render
from .models import Team
# Create your views here.
from django.views.generic import ListView


class TeamListView(ListView):
    model = Team
    template_name = "team_list.html"
