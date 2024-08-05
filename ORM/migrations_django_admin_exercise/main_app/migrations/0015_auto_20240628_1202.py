from django.db import migrations

price_multiplication = 120


def calculate_price(name: str):
    return len(name) * price_multiplication


def assign_price(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()
    for smartphone in smartphones:
        smartphone.price = calculate_price(smartphone.brand)

    smartphone_model.objects.bulk_update(smartphones, ['price'])


def assign_price_default(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    default_price = smartphone_model._meta.get_field('price').default

    smartphones = smartphone_model.objects.all()
    for smartphone in smartphones:
        smartphone.price = default_price

    smartphone_model.objects.bulk_update(smartphones, ['price'])


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0014_smartphone'),
    ]

    operations = [
        migrations.RunPython(assign_price, assign_price_default)
    ]
