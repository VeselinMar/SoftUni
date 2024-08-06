from django.apps import AppConfig

from Fruitipedia import fruits


class FruitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fruitipedia.fruits'
