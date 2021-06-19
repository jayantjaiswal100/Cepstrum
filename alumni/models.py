from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class GraduationYear(models.Model):
    year = models.PositiveIntegerField()

    def __str__(self):
        return str(self.year)


class Branch(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class PROGRAM(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class ProfileOfIntrest(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Bio(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',related_name='alumni_bio')
    name = models.CharField(max_length=200,null=True,blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    program = models.ForeignKey(PROGRAM, on_delete=models.CASCADE)
    year_of_graduation = models.ForeignKey(GraduationYear, on_delete=models.CASCADE)
    number = models.CharField(max_length=11,default=None,null=True)
    present_work=models.CharField(max_length=100)
    present_work_org=models.CharField(max_length=250)
    facebook = models.URLField(name='facebook',default=None,null=True)
    linkedin = models.URLField(name='linkedin',default=None,null=True)
    junior_intraction = models.BooleanField(null=True)
    picture = models.CharField(name='picture',max_length=500)
    published_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    profile_of_intrest = models.ForeignKey(ProfileOfIntrest, on_delete=models.CASCADE,default="",blank=True, null=True)
    intern_experience = RichTextField(blank=True, null=True)
    club_memories = RichTextField(blank=True, null=True)
    project_memories = RichTextField(blank=True, null=True)
    por_experience = RichTextField(blank=True, null=True)
    placement_experince = RichTextField(blank=True, null=True)


    def __str__(self):
        return self.name
