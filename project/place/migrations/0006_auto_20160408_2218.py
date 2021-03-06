# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_auto_20160403_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='code',
        ),
        migrations.AddField(
            model_name='category',
            name='plural',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='place',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belong_to_category', to='place.Category'),
        ),
        migrations.AddField(
            model_name='place',
            name='has_good_image',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='place',
            name='is_paying',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='place',
            name='is_verified',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='place',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'ACTIVE'), (2, 'SUSPENDED'), (3, 'REPORTED'), (4, 'DISABLED')], default=1, null=True),
        ),
    ]
