from django.db import models
from django.utils.timezone import now
# Create your models here.
class Inphase(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='inphase', max_length=100)
    pic = models.ImageField(upload_to='inphase', height_field=None, width_field=None, max_length=None,default="")
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

   
