from django.db import models


class Pingback(models.Model):
    
    repository = models.CharField(
        default='pypi',
        choices=[('pypi', 'PyPI')],
        max_length=12,
    )
    
    package_name = models.CharField(
        max_length=256,
    )
    
    last_seen = models.DateTimeField(auto_now=True)

    count = models.PositiveIntegerField(default=0)


class PingbackIP(models.Model):
    
    pingback = models.ForeignKey(Pingback)
    ip = models.GenericIPAddressField()
    last_seen = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField(default=0)
