from importlib.metadata import requires
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    age = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    height = models.IntegerField(
        'height(cm)',
        validators=[
            MaxValueValidator(250),
            MinValueValidator(1)
        ]
    )

    daily_calories_goal = models.IntegerField(
        'Daily Calories Goal(cal)',
        validators=[
            MaxValueValidator(20000),
            MinValueValidator(1)
        ]
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse('profile_detail')

    def checkedin_for_today(self):
        return HealthRecord.objects.filter(user=self.user).filter(date=date.today()).count() == 1

    def get_today_record_id(self):
        return HealthRecord.objects.filter(user=self.user).filter(date=date.today()).first().id

    def calculate_calories_remaining(self):
        foods = Food.objects.filter(user=self.user, date=date.today())
        total_calories = 0
        for food in foods:
            total_calories+=food.calories
        return self.daily_calories_goal - total_calories

class Food(models.Model):
    date = models.DateField('food date', default=date.today)
    name = models.CharField(max_length = 50)
    calories = models.IntegerField('Calories')
    protein = models.IntegerField('Protein(g)')
    fats = models.IntegerField('Fat(g)')
    carbohydrates = models.IntegerField('Carbs(g)')
    sodium = models.IntegerField('Sodium(mg)')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        return f"{self.name}"    

    def get_absolute_url(self):
        return reverse('profile_detail')
        
class HealthRecord(models.Model):
    date = models.DateField('date', default=date.today)
    weight = models.IntegerField(
        'weight(kg)',
        validators=[
            MaxValueValidator(200),
            MinValueValidator(1)
        ]
    )
    bodyfat = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile_detail')

    def __str__(self): 
        return f"{self.date}"
