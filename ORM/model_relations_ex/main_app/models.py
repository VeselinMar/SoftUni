from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(
        max_length=40,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
    )


class Song(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    songs = models.ManyToManyField(
        Song,
        related_name='artists',
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    description = models.TextField(
        max_length=200,
    )

    rating = models.PositiveSmallIntegerField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    def __str__(self):
        return self.description


class Driver(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )


class DrivingLicense(models.Model):
    license_number = models.CharField(
        max_length=10,
        unique=True,
    )

    issue_date = models.DateField()

    driver = models.OneToOneField(
        Driver,
        on_delete=models.CASCADE,
        related_name='license',
    )


class Owner(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(
        max_length=50,
    )

    year = models.PositiveSmallIntegerField()

    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='cars'
    )

    def __str__(self):
        return self.model


class Registration(models.Model):
    registration_number = models.CharField(
        max_length=10,
        unique=True,
    )

    registration_date = models.DateField(
        blank=True,
        null=True,
    )

    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='registration'
    )

    def __str__(self):
        return self.registration_number

