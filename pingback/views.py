from datetime import datetime, timedelta
from . import models
from django.http.response import HttpResponse


def pingback(request, repository=None, package=None):
    
    assert repository and package
    
    # Normalize as PyPI does: Replace _ with -
    package = package.replace("_", "-")
    
    ip = request.META['REMOTE_ADDR']
    
    # Flood protection
    flood_window = datetime.now() - timedelta(minutes=10)
    
    ip_activity = models.PingbackIP.objects.filter(
        ip=ip, last_seen__gte=flood_window)
    
    if ip_activity.count() > 30:
        return HttpResponse("Flood protection active, bye!")
    
    pingback, __ = models.Pingback.objects.get_or_create(
        package_name=package,
        repository=repository
    )
    
    pingback_ip, created = models.PingbackIP.objects.get_or_create(ip=ip, pingback=pingback)
    pingback_ip.count += 1
    pingback_ip.save()

    # If the IP is new, we increment this counter!
    if created:
        pingback.unique_count += 1
    pingback.count += 1
    pingback.save()

    return HttpResponse(
        "Pingback from package {} in repository {}".format(package, repository)
    )
