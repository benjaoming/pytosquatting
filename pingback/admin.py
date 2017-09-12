from django.contrib import admin


from . import models


@admin.register(models.Pingback)
class PingbackAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'count', 'last_seen')
    list_filter = ('repository',)


@admin.register(models.PingbackIP)
class PingbackIPAdmin(admin.ModelAdmin):
    pass
