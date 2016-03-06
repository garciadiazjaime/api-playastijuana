from rest_framework import viewsets

from ..models import Category, Place
from .serializers import CategorySerializer, PlaceSerializer

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    queryset = Category.objects.all()
    return queryset.order_by('id')

class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

  def get_queryset(self):
    queryset = Place.objects.all()
    return queryset.order_by('id')
