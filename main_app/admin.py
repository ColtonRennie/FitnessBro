from django.contrib import admin

from .models import Food, HealthRecord, Profile

admin.site.register(Profile)
admin.site.register(Food)
admin.site.register(HealthRecord)