from django.contrib import admin

from .models import Category, Place, Link

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class LinkAdmin(admin.ModelAdmin):
	list_display = ('id', 'type', 'url', 'place')
	list_filter = ('type',)

class ChoiceLink(admin.StackedInline):
	model = Link
	extra = 3

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'code', 'name', 'latitud', 'longitude')
	search_fields = ['code', 'name']
	inlines = [ChoiceLink]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Link, LinkAdmin)
