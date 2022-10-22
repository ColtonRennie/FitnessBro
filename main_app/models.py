from importlib.metadata import requires
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
    def __str__(self): 
        return f"{self.user.username}"



class Food(models.Model):
    name = models.CharField(max_length = 50)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    sodium = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self): 
        return f"{self.name}"    
        
