from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile



# Create the form class.
class StudentForm(forms.ModelForm):

    number = forms.CharField(min_length=10, max_length=10,label="Please enter Your Mobile Mumber")
    linkedin = forms.URLField(label="Link to your Linkedin handle")
    
    class Meta:
        model = Student
        fields = ['name','program','branch','year','selected_company','profile','linked_profile','resource','resume','number']  # Picture is manual
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            'program' : forms.Select(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            # 'intrest' : SearchableSelect(model='bios.Intrest',search_field='name'),
            # 'project' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'tech_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'cult_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'sport_club' : forms.SelectMultiple(attrs={'class':'form-control'}),

        }
        # labels = {
        #     "name": "Name *",
        #     "branch": "Branch *",
        #     "program": "Program *",
        #     "year_of_graduation": "Year of Graduation *",
        #     "present_work": "Current area of work *",
        #     "present_work_org": "Current University/Company/Post *",
        #     "junior_intraction":"Are you interested in interacting or helping your juniors *",
        #     "picture":"Please enter the link of the image *",
        # }
    # Validate the size of the picture

