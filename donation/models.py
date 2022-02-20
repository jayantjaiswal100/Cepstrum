from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=256)
    desc = RichTextField()
    def __str__(self):
        return self.name

class Donation(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.IntegerField()
    amount = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.owner.username

    def __unicode__(self):
        return self.owner.username
