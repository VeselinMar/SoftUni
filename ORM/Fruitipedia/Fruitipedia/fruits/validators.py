import re

from django.core.exceptions import ValidationError


class IsOnlyLettersValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'Fruitipedia.fruits.validators.IsOnlyLettersValidator',
            (),
            {'message': self.message}
        )
