from django.db import models

# Create your models here.
class Talk(models.Model):
    name = models.CharField(max_length=256)
    pic = models.URLField(max_length=400)

    def __str__(self):
        return self.name

class HomeCarousel(models.Model):
    name = models.CharField(max_length=256)
    pic = models.URLField(max_length=400)

    def __str__(self):
        return self.name