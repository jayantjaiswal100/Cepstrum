from django.contrib import admin
from bios.models import Bio,Branch,Program,Year, Projects, Intrest,TechSkill, TechClub, CultClub, SportClub
# Register your models here.
admin.site.register(Bio)
admin.site.register(Projects)
admin.site.register(Branch)
admin.site.register(Program)
admin.site.register(Year)
admin.site.register(Intrest)
admin.site.register(TechClub)
admin.site.register(TechSkill)
admin.site.register(CultClub)
admin.site.register(SportClub)
