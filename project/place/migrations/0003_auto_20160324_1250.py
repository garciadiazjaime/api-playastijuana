# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20160306_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='categories',
            field=models.ManyToManyField(to='place.Category'),
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='place.Place'),
        ),
    ]
