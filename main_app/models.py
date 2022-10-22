from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    age = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    height = models.IntegerField(
        validators=[
            MaxValueValidator(250),
            MinValueValidator(1)
        ]
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
