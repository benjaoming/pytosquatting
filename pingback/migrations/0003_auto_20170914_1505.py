# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 15:05
from __future__ import unicode_literals

from django.db import migrations, models


def populate_unique_count(apps, schema):
    Pingback = apps.get_model('pingback', 'Pingback')
    for p in Pingback.objects.all():
        p.unique_count = p.pingbackip_set.all().count()
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pingback', '0002_auto_20170912_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='pingback',
            name='unique_count',
            field=models.PositiveIntegerField(default=0, help_text='Uniqiue IPs counted', verbose_name='Unique IPs'),
        ),
        migrations.AlterField(
            model_name='pingback',
            name='count',
            field=models.PositiveIntegerField(default=0, help_text='Non-unique hits for this pingback', verbose_name='Hits'),
        ),
        migrations.RunPython(populate_unique_count, reverse_code=lambda *_: None)
    ]