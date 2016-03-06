from rest_framework import serializers

from ..models import Category, Place

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ('id', 'name')

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Place
		fields = ('id', 'name', 'latitud', 'longitude', 'code', 'categories', 'status')
