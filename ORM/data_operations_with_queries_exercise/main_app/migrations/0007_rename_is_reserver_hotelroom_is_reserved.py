# Generated by Django 5.0.4 on 2024-07-04 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_hotelroom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelroom',
            old_name='is_reserver',
            new_name='is_reserved',
        ),
    ]
