import re

from django.core.exceptions import ValidationError


def IsValidLetterString(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
