from django.contrib import admin
from .models import Category, Course, Year

# Register your models here.
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(Category)
# admin.site.register(Upload)

