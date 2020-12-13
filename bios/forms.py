from django import forms
from bios.models import Bio,Intrest,Projects,TechClub,CultClub,SportClub,TechSkill
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.files.uploadedfile import InMemoryUploadedFile
from bios.humanize import naturalsize


# Create the form class.
class BioForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    intrest = forms.ModelMultipleChoiceField(
            queryset=Intrest.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Check your Field of Intrest * (if you didn't find your intrest then create the one)"
            )
    tech_club = forms.ModelMultipleChoiceField(
            queryset=TechClub.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Technical Club You Joined *"
            )
    cult_club = forms.ModelMultipleChoiceField(
            queryset=CultClub.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Cultural Club You Joined *"
            )
    project = forms.ModelMultipleChoiceField(
            queryset=Projects.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Check the Projects You have done * (if you didn't find your project then create the one) "
            )
    sport_club = forms.ModelMultipleChoiceField(
            queryset=SportClub.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Sports Club You Joined *"
            )
    number = forms.CharField(min_length=10, max_length=10, required=False,label="Please enter Your Mobile Mumber")

    facebook = forms.URLField(required=False, label="Link to your Facebook handle")
    instagram = forms.URLField(required=False, label="Link to your Instagram handle")
    linkedin = forms.URLField(required=False, label="Link to your Linkedin handle")
    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Bio
        fields = ['name', 'branch', 'program','year','intrest','project','tech_club','cult_club','sport_club' ,'text','number','picture','facebook','linkedin','instagram']  # Picture is manual
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'branch' : forms.Select(attrs={'class':'form-control'}),
            'program' : forms.Select(attrs={'class':'form-control'}),
            'year' : forms.Select(attrs={'class':'form-control'}),
            # 'intrest' : SearchableSelect(model='bios.Intrest',search_field='name'),
            # 'project' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'tech_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'cult_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            # 'sport_club' : forms.SelectMultiple(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'editable'}),

        }
        labels = {
            "name": "Name *",
            "branch": "Branch *",
            "program": "Program *",
            "year": "Year *",
            "text": "Add Some More info....",
        }
    # Validate the size of the picture
    def clean(self) :
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None : return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    # def save(self, commit=True) :
    #     instance = super(BioForm, self).save(commit=False)
    #
    #     # We only need to adjust picture if it is a freshly uploaded file
    #     f = instance.picture   # Make a copy
    #     if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
    #         bytearr = f.read();
    #         instance.content_type = f.content_type
    #         instance.picture = bytearr  # Overwrite with the actual image data
    #
    #     if commit:
    #         instance.save()
    #     return instance

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

class IntrestForm(forms.ModelForm):
    class Meta:
        model = Intrest
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }

class TechSkillForm(forms.ModelForm):
    class Meta:
        model = TechSkill
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    techskill = forms.ModelMultipleChoiceField(
            queryset=TechSkill.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )
    class Meta:
        model = Projects
        fields = ['name','techskill','desc']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }
