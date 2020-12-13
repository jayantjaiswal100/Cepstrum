from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts import models
from accounts.models import User

class UserCreateForm(UserCreationForm):
    """docstring for UserCreateForm."""
    class Meta:
            fields = ('username','email','password1','password2')
            model = get_user_model()

    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

