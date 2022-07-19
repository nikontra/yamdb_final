from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    now = timezone.now()
    if value > now.year:
        raise ValidationError('Укажите корректный год создания произведения!')
    return value
