from django.db import models
from django.contrib.auth.models import User


class CalorieProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.FloatField(help_text="Weight in kilograms")
    height_cm = models.FloatField(help_text="Height in centimeters")

    bmr = models.FloatField(default=0)
    daily_calories = models.FloatField(default=0)

    def __str__(self):
        return self.name