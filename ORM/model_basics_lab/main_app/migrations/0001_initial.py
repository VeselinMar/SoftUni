# Generated by Django 5.0.4 on 2024-06-22 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employees_count', models.PositiveIntegerField(default=1, verbose_name='Employees Count')),
                ('location', models.CharField(choices=[('Sofia', 'Sofia'), ('Plovdiv', 'Plovdiv'), ('Varna', 'Varna'), ('Burgas', 'Burgas')], max_length=20)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('photo', models.URLField()),
                ('birth_date', models.DateField()),
                ('works_full_time', models.BooleanField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
