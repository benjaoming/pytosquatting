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

    first_seen = models.DateTimeField(auto_now_add=True)

    count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return "{}/{}".format(self.repository, self.package_name)


class PingbackIP(models.Model):
    
    pingback = models.ForeignKey(Pingback)
    ip = models.GenericIPAddressField()
    first_seen = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField(default=0)
