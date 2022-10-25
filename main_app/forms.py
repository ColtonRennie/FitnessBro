from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'age', 'height', "username", "email"]
    
    def save(self, commit=True):
        age = self.cleaned_data['age']
        height = self.cleaned_data['height']
        user = super(UserForm, self).save()
        Profile.objects.create(age=age, user=user, height=height)
        return user