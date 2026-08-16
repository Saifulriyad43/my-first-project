from django.contrib import admin
from .models import CalorieProfile


@admin.register(CalorieProfile)
class CalorieProfileAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'age',
        'gender',
        'weight',
        'height_cm',
        'bmr',
        'daily_calories'
    )