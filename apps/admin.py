from django.contrib import admin

from apps.models import Region, District, Product, Category


@admin.register(Region)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(District)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'description']
    autocomplete_fields = ['category']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
