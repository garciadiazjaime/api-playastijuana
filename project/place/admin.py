from django.contrib import admin

from .models import Category, Place, Link, Image

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class ChoiceLink(admin.StackedInline):
	model = Link
	extra = 3

class ChoiceImage(admin.StackedInline):
	model = Image
	extra = 1

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'latitud', 'longitude', 'category', 'status', 'is_verified', 'has_good_image', 'weight', 'is_paying')
	search_fields = ['id', 'name']
	inlines = [ChoiceLink, ChoiceImage]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
