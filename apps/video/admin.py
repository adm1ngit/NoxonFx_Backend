from django.contrib import admin
from .models import VideoApp, ModulClass, Comment


class ModulAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    list_filter = ('name',)


admin.site.register(ModulClass, ModulAdmin)


class VideoAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'modul', 'name',)
    list_display_links = ('id', 'modul', 'name',)
    list_filter = ('name',)


admin.site.register(VideoApp, VideoAppAdmin)
admin.site.register(Comment)
