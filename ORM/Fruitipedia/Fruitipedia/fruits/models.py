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


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2),
                    IsOnlyLettersValidator],
        help_text='Enter only letters - length between 2 and 30',
        blank=False,
        null=False,
    )

    Image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True
    )
