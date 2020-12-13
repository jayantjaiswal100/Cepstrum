from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    """docstring for User."""
    def __str__(self):
        return "@{}".format(self.username)
        return "{}".format(self.email)
