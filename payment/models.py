from django.core.exceptions import ValidationError
from django.db import models


def validate_positive(value):
    if value <= 0:
        raise ValidationError(
            (f'{value} is not a positive number'),
        )

class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    stripe_price_id = models.CharField(max_length=100)