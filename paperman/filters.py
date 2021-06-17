from django.db import models
from django.db.models import fields, query
from django.forms import widgets
import django_filters
from .models import Course,Category, PaperMan,Year
from django import forms

class PapermanFilter(django_filters.FilterSet):
    course = django_filters.ModelMultipleChoiceFilter(
        queryset = Course.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    year = django_filters.ModelMultipleChoiceFilter(
        queryset = Year.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    category = django_filters.ModelMultipleChoiceFilter(
        queryset = Category.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
        model = PaperMan
        fields = {

            'year':['exact'],
        }