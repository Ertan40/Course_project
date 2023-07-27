from django.core.exceptions import ValidationError


def validate_only_numbers(value):
    for char in value:
        if not char.isdigit():
            raise ValidationError("Phone number must contain only numbers.")