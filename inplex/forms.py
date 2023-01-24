from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create the form class.
class StudentForm(forms.ModelForm):

    number = forms.CharField(min_length=10, max_length=10,label="Please enter Your Mobile Mumber",required=False)
    # linkedin = forms.URLField(label="Link to your Linkedin handle")
    
    class Meta:
        model = Student
        fields = ['name','program','branch','year','selected_company','profile','linked_in_profile','resource','resume','number']  # Picture is manual
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            'program' : forms.Select(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),

        }
        labels = {
            "selected_company": "Upcoming Intern/Interned at",
            "resource":"Resources you used while your preparation",
            "resume":"Resume Link",
            "linked_in_profile":"LinkedIn profile"
        }
    # Validate the size of the picture



class ExperienceForm(forms.ModelForm):

    # difficulty1 = forms.IntegerField()
    class Meta:
        model = Experience
        fields = ["company" ,"profile" ,"roundtype1","experience1" ,"difficulty1" ,"roundtype2","experience2" ,"difficulty2" ,"roundtype3" ,"difficulty3","experience3","roundtype4","experience4","difficulty4","roundtype5","experience5","difficulty5","roundtype6","experience6","difficulty6","roundtype7","experience7" ,"difficulty7",'year','selected']
        widgets = {
           'difficulty1':  forms.RadioSelect(),
           'difficulty2':  forms.RadioSelect(),
        }
        labels = {
            'roundtype1': 'Type',
            'roundtype2': 'Type',
            'roundtype3': 'Type',
            'roundtype4': 'Type',
            'roundtype5': 'Type',
            'roundtype6': 'Type',
            'roundtype7': 'Type',
            'difficulty1': 'Difficulty',
            'difficulty2': 'Difficulty',
            'difficulty3': 'Difficulty',
            'difficulty4': 'Difficulty',
            'difficulty5': 'Difficulty',
            'difficulty6': 'Difficulty',
            'difficulty7': 'Difficulty',
            'experience1': 'Experience',
            'experience2': 'Experience',
            'experience3': 'Experience',
            'experience4': 'Experience',
            'experience5': 'Experience',
            'experience6': 'Experience',
            'experience7': 'Experience',
            'selected': 'Yes',
        }

