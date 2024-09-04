from django.contrib import admin
from plays.models import Play
# Register your models here.

admin.site.register(Play, admin.ModelAdmin)
