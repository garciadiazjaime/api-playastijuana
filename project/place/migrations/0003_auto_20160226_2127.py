# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20160226_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='place.Category'),
        ),
    ]
