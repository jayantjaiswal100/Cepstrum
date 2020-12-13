from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Intrest(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class TechSkill(models.Model):
        name = models.CharField(max_length=256)

        def __str__(self):
            return self.name

class Projects(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=106)
    desc = models.TextField(null=True,blank=True)
    techskill = models.ManyToManyField(TechSkill)

    def __str__(self):
        return self.name

class TechClub(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class CultClub(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class SportClub(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Bio(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=200,null=True,blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    intrest = models.ManyToManyField(Intrest)
    project = models.ManyToManyField(Projects)
    tech_club = models.ManyToManyField(TechClub, blank=True)
    cult_club = models.ManyToManyField(CultClub, blank=True)
    sport_club = models.ManyToManyField(SportClub, blank=True)
    number = models.CharField(max_length=11,default=None,null=True)
    text = models.TextField(max_length=520)
    facebook = models.URLField(name='facebook',default=None,null=True)
    linkedin = models.URLField(name='linkedin',default=None,null=True)
    instagram = models.URLField(name='instagram',default=None,null=True)
    picture = models.CharField(name='picture',max_length=500)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
