from django.contrib import admin
from .models import GraduationYear, Branch, PROGRAM,Bio
# Register your models here.
admin.site.register(Bio)
admin.site.register(PROGRAM)
admin.site.register(Branch)
admin.site.register(GraduationYear)
