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
	list_display = ('id', 'code', 'name', 'latitud', 'longitude', 'status')
	search_fields = ['id', 'code', 'name']
	inlines = [ChoiceLink, ChoiceImage]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
