from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    plural = models.CharField(max_length=150, default='')

    def __unicode__(self):
        return "%s" % (self.name)

class Place(models.Model):
    STATUS_CHOICES = (
        (1, 'ACTIVE'),
        (2, 'SUSPENDED'),
        (3, 'REPORTED'),
        (4, 'DISABLED'),
    )
    name = models.CharField(max_length=120)
    latitud = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    categories = models.ManyToManyField(Category)
    category = models.ForeignKey(Category, related_name='belong_to_category', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, blank=True, null=True)
    is_verified = models.IntegerField(default=0)
    has_good_image = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    is_paying = models.IntegerField(default=0)

    def __unicode__(self):
		return "%s" % (self.name)

class Image(models.Model):
    TYPE_CHOICES = (
        ('COVER', 'COVER'),
        ('BANNER', 'BANNER'),
    )
    url = models.URLField(max_length=500, default='')
    place = models.ForeignKey(Place, default='')
    type = models.CharField(choices=TYPE_CHOICES, default='COVER', max_length=20)

    def __unicode__(self):
        return "%s" % self.url

class Link(models.Model):
    url = models.URLField(max_length=500)
    place = models.ForeignKey(Place, default='')

    def __unicode__(self):
        return "%s" % self.url
