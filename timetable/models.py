from turtle import mode
from django.db import models

# Create your models here.
days=['mon','tue','wed','thur','fri']
slots=['8_9','9_10','10_11','11_12','12_1','2_3','3_4','4_5']
class Timetable(models.Model):
    roll_number=models.IntegerField(primary_key=True)
    year=models.IntegerField(default=18)
    branch = models.IntegerField(default=0)
    mon_8_9 = models.CharField(max_length=41, default='', blank=True)
    mon_9_10 = models.CharField(max_length=41, default='', blank=True)
    mon_10_11 = models.CharField(max_length=41, default='', blank=True)
    mon_11_12 = models.CharField(max_length=41, default='', blank=True)
    mon_12_1 = models.CharField(max_length=41, default='', blank=True)
    mon_2_3 = models.CharField(max_length=41, default='', blank=True)
    mon_3_4 = models.CharField(max_length=41, default='', blank=True)
    mon_4_5 = models.CharField(max_length=41, default='', blank=True)
    tue_8_9 = models.CharField(max_length=41, default='', blank=True)
    tue_9_10 = models.CharField(max_length=41, default='', blank=True)
    tue_10_11 = models.CharField(max_length=41, default='', blank=True)
    tue_11_12 = models.CharField(max_length=41, default='', blank=True)
    tue_12_1 = models.CharField(max_length=41, default='', blank=True)
    tue_2_3 = models.CharField(max_length=41, default='', blank=True)
    tue_3_4 = models.CharField(max_length=41, default='', blank=True)
    tue_4_5 = models.CharField(max_length=41, default='', blank=True)
    wed_8_9 = models.CharField(max_length=41, default='', blank=True)
    wed_9_10 = models.CharField(max_length=41, default='', blank=True)
    wed_10_11 = models.CharField(max_length=41, default='', blank=True)
    wed_11_12 = models.CharField(max_length=41, default='', blank=True)
    wed_12_1 = models.CharField(max_length=41, default='', blank=True)
    wed_2_3 = models.CharField(max_length=41, default='', blank=True)
    wed_3_4 = models.CharField(max_length=41, default='', blank=True)
    wed_4_5 = models.CharField(max_length=41, default='', blank=True)
    thur_8_9 = models.CharField(max_length=41, default='', blank=True)
    thur_9_10 = models.CharField(max_length=41, default='', blank=True)
    thur_10_11 = models.CharField(max_length=41, default='', blank=True)
    thur_11_12 = models.CharField(max_length=41, default='', blank=True)
    thur_12_1 = models.CharField(max_length=41, default='', blank=True)
    thur_2_3 = models.CharField(max_length=41, default='', blank=True)
    thur_3_4 = models.CharField(max_length=41, default='', blank=True)
    thur_4_5 = models.CharField(max_length=41, default='', blank=True)
    fri_8_9 = models.CharField(max_length=41, default='', blank=True)
    fri_9_10 = models.CharField(max_length=41, default='', blank=True)
    fri_10_11 = models.CharField(max_length=41, default='', blank=True)
    fri_11_12 = models.CharField(max_length=41, default='', blank=True)
    fri_12_1 = models.CharField(max_length=41, default='', blank=True)
    fri_2_3 = models.CharField(max_length=41, default='', blank=True)
    fri_3_4 = models.CharField(max_length=41, default='', blank=True)
    fri_4_5 = models.CharField(max_length=41, default='', blank=True)

    def __str__(self):
        return str(self.roll_number)
    
