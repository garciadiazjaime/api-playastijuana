from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    plural = models.CharField(max_length=150, default='')
    position = models.IntegerField(default=0)

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
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    category = models.ForeignKey(Category, related_name='belong_to_category', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, blank=True, null=True)
    is_verified = models.IntegerField(default=0)
    has_good_image = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    is_paying = models.IntegerField(default=0)
    has_links = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def __unicode__(self):
		return "%s" % (self.name)

    def save(self, *args, **kwargs):
        score = round((self.is_verified + self.has_good_image + self.weight + self.is_paying + (self.has_links / 3.0)) / 5.0, 2) * 100
        self.score = score
        super(Place, self).save(*args, **kwargs)

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
