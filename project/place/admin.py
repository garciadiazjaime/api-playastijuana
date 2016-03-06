from django.contrib import admin

from .models import Category, Place, Link

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id', 'code', 'name', 'latitud', 'longitude', 'status')
	search_fields = ['code', 'name']

class LinkAdmin(admin.ModelAdmin):
	list_display = ('id', 'type', 'url', 'place')
	list_filter = ('type',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Link, LinkAdmin)
