from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return "%s" % (self.name)

class Place(models.Model):
    STATUS_TYPES = (
        (1, 'CREATED'),
        (2, 'GMAPS_VERIFIED'),
        (3, 'REAL_VERIFIED'),
        (4, 'SUSPENDED'),
        (5, 'REPORTED'),
        (6, 'DISABLED'),
    )
    name = models.CharField(max_length=120)
    latitud = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    code = models.CharField(max_length=120, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    status = models.IntegerField(choices=STATUS_TYPES, default=1)

    def __unicode__(self):
		return "%s - %s" % (self.name)

class Link(models.Model):
    LINK_TYPES = (
        (1, 'GMAPS'),
        (2, 'FACEBOOK'),
        (3, 'WEBSITE'),
        (4, 'FOURSQUARE'),
        (5, 'YELP'),
    )
    type = models.IntegerField(choices=LINK_TYPES)
    url = models.URLField(max_length=500)
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return "%s" % self.type
