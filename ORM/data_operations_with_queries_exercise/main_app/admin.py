from django.contrib import admin

from main_app.models import Pet, Artifact, Location, Car, Task


# Register your models here.


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species']
    list_filter = ['species']
    search_fields = ['name', 'species']


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin', 'age', 'description']
    list_filter = ['is_magical']
    search_fields = ['name', 'origin', 'age', 'is_magical']
    readonly_fields = ['is_magical']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'population', 'description', 'is_capital']
    list_filter = ['region', 'is_capital']
    search_fields = ['name', 'region', 'is_capital']
    readonly_fields = ['is_capital']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'year', 'color', 'price', 'price_with_discount']
    list_filter = ['model', 'year']
    search_fields = ['model', 'year', 'color', 'price']
    readonly_fields = ['price_with_discount']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'is_finished']
    list_filter = ['is_finished']
    search_fields = ['title', 'is_finished']
    readonly_fields = ['is_finished']