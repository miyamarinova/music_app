from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from music_app.profile.models import Profile


# Create your models here.
class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    GENRE_CHOICES = ["Pop Music", "Jazz Music", "R&B Muxic"]
    MIN_PRICE = 0.0
    MAX_GENRE_LENGTH = 30

    GENRES = {
        "GENRE_POP_MUSIC": "Pop Music",
        "GENRE_JAZ_MUSIC": "Jazz Music",
        "GENRE_RNB_MUSIC": "R&B Music",
        "GENRE_ROCK_MUSIC": "Rock Music",
        "GENRE_COUNTRY_MUSIC": "Country Music",
        "GENRE_DANCE_MUSIC": "Dance Music",
        "GENRE_HIP_HO_MUSIC": "Hip Hop Music",
        "GENRE_OTHER": "Other"
    }


    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        unique=True,
        verbose_name="Album Name"
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist Name"
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

