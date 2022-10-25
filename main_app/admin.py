from django.contrib import admin

from .models import Food, Profile

admin.site.register(Profile)
admin.site.register(Food)