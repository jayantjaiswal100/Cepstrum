from django.db import models

# Create your models here.
class Celebration(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    pic = models.ImageField(upload_to='celebration_list', height_field=None, width_field=None, max_length=None,null=True)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Pictures(models.Model):
    celebration = models.OneToOneField(Celebration, on_delete=models.CASCADE)
    year = models.OneToOneField(Year, on_delete=models.CASCADE)
    pic1 = models.URLField(default=None)
    pic2 = models.URLField(default=None)
    pic3 = models.URLField(default=None)
    pic4 = models.URLField(default=None)
    pic5 = models.URLField(default=None)
    pic6 = models.URLField(default=None)
    pic7 = models.URLField(default=None)
    pic8 = models.URLField(default=None)

    def __str__(self):
        return self.celebration.name
