from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.
def validate_username(value):
    if not value.isalnum() or "_" in value:
        raise ValidationError("Username contains only letters, numbers, and underscores.")

class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[validate_username, MinLengthValidator(limit_value=2)],
        )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        blank=True,
        validators=[MinValueValidator(limit_value=0)]
    )

