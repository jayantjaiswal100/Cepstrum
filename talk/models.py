from django.db import models

# Create your models here.
class Talk(models.Model):
    name = models.CharField(max_length=256)
    pic1 = models.ImageField(upload_to='talk_list', height_field=None, width_field=None, max_length=None,null=True)


    def __str__(self):
        return self.name

class HomeCarousel(models.Model):
    name = models.CharField(max_length=256)
    pic1 = models.ImageField(upload_to='talk_list', height_field=None, width_field=None, max_length=None,null=True)

    def __str__(self):
        return self.name