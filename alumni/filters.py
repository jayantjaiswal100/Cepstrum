import django_filters
from .models import Bio
from django import forms

class AlumniFilter(django_filters.FilterSet):
    class Meta:
        model = Bio
        fields = {
        'name': ['icontains'],
        'present_work': ['icontains'],
        'present_work_org': ['icontains'],
        'branch':['exact'],
        'program': ['exact'],
        'year_of_graduation':['exact'],
        }
