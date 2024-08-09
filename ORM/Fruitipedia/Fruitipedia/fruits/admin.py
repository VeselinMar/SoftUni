from django.contrib import admin

from Fruitipedia.fruits.models import Fruit


# Register your models here.

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_filter = ['category',]
    search_fields = ['name', 'category']
