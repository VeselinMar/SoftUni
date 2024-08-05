from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

from main_app.managers import AstronautManager


def validate_digits(value):
    if not value.isdigit():
        raise ValidationError('This field must contain only digits.')


class Astronaut(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[validate_digits],
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    date_of_birth = models.DateField(null=True, blank=True)

    spacewalks = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    updated_at = models.DateTimeField(auto_now=True)

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.SmallIntegerField(
        validators=[MinValueValidator(1)],
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.manufacturer})"


class Mission(models.Model):
    class StatusChoices(models.TextChoices):
        PLANNED = 'Planned', 'Planned'
        ONGOING = 'Ongoing', 'Ongoing'
        COMPLETED = 'Completed', 'Completed'

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=9,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANNED,
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(auto_now=True)

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
    )

    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='missions'
    )

    commander = models.ForeignKey(
        to=Astronaut,
        related_name='missions_as_commander',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} ({self.status})"
