import time

from django.core.management import call_command
from django.core.management.base import BaseCommand


from pingback import models


class Command(BaseCommand):

    def handle(self, *args, **options):

        pingbacks = models.Pingback.objects.filter(repository='pypi').order_by('package_name')
        for pingback in pingbacks:
            call_command('createpackage', pingback.package_name)
            print("\nSleeping 2 secs...\n")
            time.sleep(2)
