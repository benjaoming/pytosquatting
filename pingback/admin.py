from django.contrib import admin


from . import models


@admin.register(models.Pingback)
class PingbackAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'unique_count', 'count', 'last_seen', 'first_seen')
    list_filter = ('repository', 'last_seen')


@admin.register(models.PingbackIP)
class PingbackIPAdmin(admin.ModelAdmin):
    list_display = ('ip', 'count', 'last_seen', 'pingback')
