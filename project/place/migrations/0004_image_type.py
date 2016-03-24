# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20160324_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='type',
            field=models.CharField(choices=[('COVER', 'COVER'), ('BANNER', 'BANNER')], default='COVER', max_length=20),
        ),
    ]
