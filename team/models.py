from django.db import models


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50)
  

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=50)
  

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
  

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    facebook = models.URLField(max_length=200,null=True,blank=True)
    linkeden = models.URLField(max_length=200,null=True,blank=True)
    pic = models.ImageField(upload_to='team', height_field=None, width_field=None, max_length=None,default="")


    def __str__(self):
        return self.name

class PrevTeam(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    linkedin = models.URLField(max_length=200,null=True,blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE,related_name='year')
    def __str__(self):
        return self.name