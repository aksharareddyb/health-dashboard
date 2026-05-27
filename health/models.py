from django.db import models

class Workout(models.Model):
    duration = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class Meal(models.Model):
    calories = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class Sleep(models.Model):
    hours = models.FloatField()
    date = models.DateField(auto_now_add=True)

class HealthData(models.Model):
    workout = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    sleep = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at.date()} - Workout: {self.workout}"