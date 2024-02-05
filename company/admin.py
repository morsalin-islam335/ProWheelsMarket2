from django.contrib import admin

# Register your models here.

from .models import Category


class CategorySlug(admin.ModelAdmin):
    prepopulated_fields = {"slug":('brand',)}
    display = ['slug', 'brand']

admin.site.register(Category, CategorySlug)

