# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_auto_20160408_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='type',
        ),
    ]