from django.contrib import admin
from plays.models import Play, Actor, Show

class ShowAdminInLine(admin.StackedInline):
    model = Show
    extra = 0

class PlayAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [ShowAdminInLine]



admin.site.register(Play, PlayAdmin)
admin.site.register(Actor, admin.ModelAdmin)
admin.site.register(Show, admin.ModelAdmin)

