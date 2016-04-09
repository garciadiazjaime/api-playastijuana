from rest_framework import serializers

from ..models import Category, Place

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name', 'plural', 'position')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'latitude', 'longitude', 'category', 'status', 'image_set', 'link_set', 'score')
        depth = 1
