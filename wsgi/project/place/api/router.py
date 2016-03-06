from rest_framework import routers

from .views import CategoryViewSet, PlaceViewSet

# Routers provide an easy way of automatically determining the URL conf.
# These are the Django Rest available routes
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'place', PlaceViewSet)
