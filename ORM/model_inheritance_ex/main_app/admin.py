from django.contrib import admin

from main_app.models import RegularReservation


# Register your models here.
@admin.register(RegularReservation)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['room', 'start_date', 'end_date']
