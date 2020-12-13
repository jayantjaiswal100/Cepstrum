import django_filters
from .models import Bio,Intrest,Projects,TechClub,CultClub,SportClub,TechSkill
from django import forms

class BioFilter(django_filters.FilterSet):
    intrest=django_filters.ModelMultipleChoiceFilter(
        queryset=Intrest.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    project=django_filters.ModelMultipleChoiceFilter(
        queryset=Projects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    tech_club=django_filters.ModelMultipleChoiceFilter(
        queryset=TechClub.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    cult_club=django_filters.ModelMultipleChoiceFilter(
        queryset=CultClub.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    sport_club=django_filters.ModelMultipleChoiceFilter(
        queryset=SportClub.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Bio
        fields = {
        'name': ['icontains'],
        'branch':['exact'],
        'program': ['exact'],
        'year':['exact'],
        'intrest': ['exact'],
        'project': ['exact'],
        'tech_club' : ['exact'],
        'cult_club' : ['exact'],
        'sport_club' : ['exact'],
        }

class ProjectFilter(django_filters.FilterSet):

    techskill=django_filters.ModelMultipleChoiceFilter(
        queryset=TechSkill.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Projects
        fields = {
        'name': ['icontains'],
        'techskill':['exact'],
        }
