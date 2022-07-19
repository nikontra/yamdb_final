from django.utils import timezone
from django.core.exceptions import ValidationError


def year_validator(value):
    now = timezone.now()
    if value > now.year:
        raise ValidationError('Укажите корректный год создания произведения!')
    return value
