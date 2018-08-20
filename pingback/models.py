from django.utils.translation import ugettext_lazy as _
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

    first_seen_blocked = models.DateTimeField(null=True, blank=True)
    blocked = models.BooleanField(default=False)

    count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Hits"),
        help_text=_("Non-unique hits for this pingback"),
    )
    
    unique_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Unique IPs"),
        help_text=_("Uniqiue IPs counted"),
    )

    def __str__(self):
        return "{}/{}".format(self.repository, self.package_name)


class PingbackIP(models.Model):
    
    pingback = models.ForeignKey(Pingback)
    ip = models.GenericIPAddressField()
    first_seen = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField(default=0)
