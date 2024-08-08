import re

from django.core.exceptions import ValidationError


class IsOnlyLettersValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value: str):
        # Check if the value matches the allowed pattern
        if not re.match('^[A-Za-z ]+$', value):
            raise ValidationError(self.message)

        # Ensure that there is at least one letter
        if not re.search('[A-Za-z]', value):
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'Fruitipedia.fruits.validators.IsOnlyLettersValidator',
            (),
            {'message': self.message}
        )
