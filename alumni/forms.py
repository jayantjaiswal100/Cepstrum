from django import forms
from alumni.models import Bio
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile
from alumni.humanize import naturalsize


# Create the form class.
class AlumniForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    number = forms.CharField(min_length=10, max_length=10,label="Please enter Your Mobile Mumber")

    facebook = forms.URLField(label="Link to your Facebook handle")
    linkedin = forms.URLField(label="Link to your Linkedin handle")
    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Bio
        fields = ['name', 'branch', 'program','year_of_graduation','number','present_work','present_work_org','junior_intraction','picture','facebook','linkedin']  # Picture is manual
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            'program' : forms.Select(attrs={'class':'form-control'}),
            'year_of_graduation' : forms.Select(attrs={'class':'form-control'}),
            # 'intrest' : SearchableSelect(model='bios.Intrest',search_field='name'),
            # 'project' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'tech_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'cult_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'sport_club' : forms.SelectMultiple(attrs={'class':'form-control'}),

        }
        labels = {
            "name": "Name *",
            "branch": "Branch *",
            "program": "Program *",
            "year_of_graduation": "Year of Graduation *",
            "present_work": "Current area of work *",
            "present_work_org": "Current University/Company/Post *",
            "junior_intraction":"Are you interested in interacting or helping your juniors *",
        }
    # Validate the size of the picture
    def clean(self) :
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None : return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")
