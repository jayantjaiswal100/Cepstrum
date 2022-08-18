from django.db import models
from bios.models import Branch, Year, Program
from django.conf import settings
from ckeditor.fields import RichTextField
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=256)


    def __str__(self):
        return self.name

# class Selected(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class RoundType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=256)
    profile = models.ManyToManyField(Profile)
    cpi = models.DecimalField(max_digits=5, decimal_places=2)
    eligible_branch = models.ManyToManyField(Branch)
    stipend = models.CharField(max_length=256,default=0)


    def __str__(self):
        return self.name

class Experience(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    roundtype1 = models.ForeignKey(RoundType, related_name='one', on_delete=models.CASCADE,null=True,blank=True)
    experince1 = RichTextField(null=True,blank=True)
    difficulty1 = models.ForeignKey(Difficulty, related_name='one', on_delete=models.CASCADE,null=True,blank=True)
    roundtype2 = models.ForeignKey(RoundType, related_name='two', on_delete=models.CASCADE,null=True,blank=True)
    experince2 = RichTextField(null=True,blank=True)
    difficulty2 = models.ForeignKey(Difficulty, related_name='two', on_delete=models.CASCADE,null=True,blank=True)
    roundtype3 = models.ForeignKey(RoundType, related_name='three', on_delete=models.CASCADE,null=True,blank=True)
    experince3 = RichTextField(null=True,blank=True)
    difficulty3 = models.ForeignKey(Difficulty, related_name='three', on_delete=models.CASCADE,null=True,blank=True)
    roundtype4 = models.ForeignKey(RoundType, related_name='four', on_delete=models.CASCADE,null=True,blank=True)
    experince4 = RichTextField(null=True,blank=True)
    difficulty4 = models.ForeignKey(Difficulty, related_name='four', on_delete=models.CASCADE,null=True,blank=True)
    roundtype5 = models.ForeignKey(RoundType, related_name='five', on_delete=models.CASCADE,null=True,blank=True)
    experince5 = RichTextField(null=True,blank=True)
    difficulty5 = models.ForeignKey(Difficulty, related_name='five', on_delete=models.CASCADE,null=True,blank=True)
    roundtype6 = models.ForeignKey(RoundType, related_name='six', on_delete=models.CASCADE,null=True,blank=True)
    experince6 = RichTextField(null=True,blank=True)
    difficulty6 = models.ForeignKey(Difficulty, related_name='six', on_delete=models.CASCADE,null=True,blank=True)
    roundtype7 = models.ForeignKey(RoundType, related_name='seven', on_delete=models.CASCADE,null=True,blank=True)
    experince7 = RichTextField(null=True,blank=True)
    difficulty7 = models.ForeignKey(Difficulty, related_name='seven', on_delete=models.CASCADE,null=True,blank=True)
    year = models.ForeignKey(Year,null=True,blank=True,on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner)

class Student(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length = 255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    selected_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    linked_profile = models.URLField()
    resource = RichTextField(null = True, blank = True)
    resume = models.URLField(null=True, blank = True)
    number = models.CharField(max_length=11,default=None,null=True)

    def __str__(self):
        return str(self.owner)

