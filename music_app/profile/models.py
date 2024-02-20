from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.
def validate_username(username):
   is_valid = all(ch.isalnum() or ch == '_' for ch in username)

   if not is_valid:
       raise ValidationError("Username contains only letters, numbers, and underscores.")

class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_USERNAME,
        validators=[validate_username, MinLengthValidator(MIN_USERNAME_LENGTH)],
        )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

