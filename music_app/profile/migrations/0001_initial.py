# Generated by Django 5.0.2 on 2024-02-19 16:34

import django.core.validators
import music_app.profile.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[music_app.profile.models.validate_username, django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
