from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.CharField(max_length=256)

    def __str__(self):
        return self.year

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# class Upload(models.Model):
#     name = models.FileField(upload_to='paperman', max_length=100)

#     def __str__(self):
#         return self.name                

class PaperMan(models.Model):
    name = models.CharField(Course, max_length=200,null=True,blank=True)
    year = models.ForeignKey(Year,on_delete=models.CASCADE,default=None,null=True)
    category = models.CharField(Category, max_length=200,null=True,blank=True)
    upload = models.FileField(upload_to='paperman', max_length=100, default=None,null=True)
    def __str__(self):
        return self.name

