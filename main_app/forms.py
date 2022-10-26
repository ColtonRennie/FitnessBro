from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    daily_calories_goal = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ["daily_calories_goal", "first_name", "last_name", 'age', 'height', "username", "email"]
    
    def save(self, commit=True):
        age = self.cleaned_data['age']
        height = self.cleaned_data['height']
        daily_calories_goal = self.cleaned_data['daily_calories_goal']
        user = super(UserForm, self).save()
        Profile.objects.create(age=age, user=user, height=height, daily_calories_goal=daily_calories_goal)
        return user