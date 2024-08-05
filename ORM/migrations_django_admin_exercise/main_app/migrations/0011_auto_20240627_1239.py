# Generated by Django 5.0.4 on 2024-06-27 12:39

from django.db import migrations


def assign_age_group(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    people = person_model.objects.all()

    for person in people:
        if person.age <= 12:
            person.age_group = "Child"
        elif person.age <= 17:
            person.age_group = "Teen"
        else:
            person.age_group = "Adult"

    person_model.objects.bulk_update(people, ['age_group'])


def assign_age_group_default(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    for person in person_model.objects.all():
        person.age_group = person_model._meta.get_field('age_group').default
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_person'),
    ]

    operations = [
        migrations.RunPython(assign_age_group, assign_age_group_default)
    ]
