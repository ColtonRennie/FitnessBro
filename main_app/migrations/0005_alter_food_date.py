# Generated by Django 4.1.1 on 2022-10-22 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_food_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='food date'),
        ),
    ]