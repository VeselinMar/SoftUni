import re
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator

from django.db import models

# Create your models here.


def letters_and_spaces_validator(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError("Name can only contain letters and spaces")


def phone_number_validator(value):
    if not re.match(r'^\+359\d{9}$', value):
        raise ValidationError("Phone number must start with '+359' followed by 9 digits")


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[letters_and_spaces_validator]
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18, 'Age must be greater than or equal to 18')]
    )

    email = models.EmailField(
        error_messages={'invalid': 'Enter a valid email address'}
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[phone_number_validator]
    )

    website_url = models.URLField(
        error_messages={'invalid': 'Enter a valid URL'}
    )


class BaseMedia(models.Model):
    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    genre = models.CharField(
        max_length=50,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        abstract = True

        ordering = ['-created_at', 'title']


class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, 'Author must be at least 5 characters long')]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, 'ISBN must be at least 6 characters long')]
    )

    class Meta(BaseMedia.Meta):

        verbose_name = "Model Book"

        verbose_name_plural = "Models of type - Book"


class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, 'Director must be at least 8 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"

        verbose_name_plural = "Models of type - Movie"


class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, 'Artist must be at least 9 characters long')]
    )

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"

        verbose_name_plural = "Models of type - Music"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def calculate_tax(self):
        return self.price * Decimal('0.08')

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('2.00')

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    def calculate_price_without_discount(self):
        return self.price * Decimal('1.2')

    def calculate_tax(self):
        return self.price * Decimal('0.05')

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal('1.50')

    def format_product_name(self):
        return f"Discounted Product: {self.name}"

    class Meta:
        proxy = True


class RechargeEnergyMixin:
    def recharge_energy(self, amount: int):
        self.energy += amount

        if self.energy > 100:
            self.energy = 100


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(
        max_length=100,
    )

    hero_title = models.CharField(
        max_length=100,
    )

    energy = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.energy <= 0:
            raise ValidationError("Energy must be a positive integer.")
        super().save(*args, **kwargs)


class SpiderHero(Hero):
    def swing_from_buildings(self):
        if self.energy < 80:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        self.energy -= 80

        if self.energy == 0:
            self.energy = 1

        self.save()

        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:

        proxy = True


class FlashHero(Hero):
    def run_at_super_speed(self):
        if self.energy < 65:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.energy -= 65

        if self.energy == 0:
            self.energy = 1

        self.save()

        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:

        proxy = True
