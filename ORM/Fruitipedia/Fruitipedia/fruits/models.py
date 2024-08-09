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


# define class fruit
class Fruit(models.Model):
    # required field (2-30) letters only
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2),
                    IsOnlyLettersValidator()],
        blank=False,
        null=False,
    )
    # required url field to an image corresponding to a fruit
    image_url = models.URLField(blank=False, null=False)
    # required TextField for fruit description
    description = models.TextField(blank=False, null=False)
    # required TextField for fruit nutrition
    nutrition = models.TextField(blank=True, null=True)
    # option ForeignKey field indicating the category a fruit belongs to
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
