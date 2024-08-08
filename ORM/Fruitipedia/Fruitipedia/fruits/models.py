from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia.fruits.validators import IsOnlyLettersValidator


# Create your models here.


class Category(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2),
                    IsOnlyLettersValidator()],
        blank=False,
        null=False,
    )

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True
    )
