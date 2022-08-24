import django_filters
from .models import *
from django import forms
from django.contrib.auth import get_user_model

class ExpFilter(django_filters.FilterSet):
    CHOICES = list(get_user_model().objects.all().values_list("id", "first_name"))
    owner = django_filters.ChoiceFilter(widget=forms.Select,choices=CHOICES)
    class Meta:
        model = Experience
        fields = {
        'company': ['exact'],
        }
