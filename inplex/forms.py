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
        fields = ['name','program','branch','year','selected_company','profile','linked_profile','resource','resume','number']  # Picture is manual
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            'program' : forms.Select(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),

        }
        labels = {
            "selected_company": "Upcoming Intern/Interned at",
            "resource":"Resources"
        }
    # Validate the size of the picture



class ExperienceForm(forms.ModelForm):

    
    class Meta:
        model = Experience
        fields = ["company" ,"profile" ,"roundtype1","experince1" ,"difficulty1" ,"roundtype2","experince2" ,"difficulty2" ,"roundtype3" ,"difficulty3","experince3","roundtype4","experince4","difficulty4","roundtype5","experince5","difficulty5","roundtype6","experince6","difficulty6","roundtype7","experince7" ,"difficulty7",'year','selected']
        widgets = {
        }
        labels = {
            'roundtype1': 'Type',
            'difficulty1': 'Difficulty',
        }
    # Validate the size of the picture
