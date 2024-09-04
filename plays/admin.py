from django.contrib import admin
from plays.models import Play


class PlayAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Play, PlayAdmin)

