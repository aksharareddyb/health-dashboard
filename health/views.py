from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Workout, Meal, Sleep, HealthData
from datetime import date
import json

def index(request):
    return render(request, 'index.html')

def health(request):
    return JsonResponse({"status": "ok"})

def history(request):
    workouts = Workout.objects.all().order_by('-date')
    meals = Meal.objects.all().order_by('-date')
    sleeps = Sleep.objects.all().order_by('-date')

    return render(request, 'history.html', {
        'workouts': workouts,
        'meals': meals,
        'sleeps': sleeps
    })

def summary(request):
    obj = HealthData.objects.first()

    return JsonResponse({
        "workout": obj.workout if obj else 0,
        "calories": obj.calories if obj else 0,
        "sleep": obj.sleep if obj else 0,
    })

def summary_page(request):
    today = date.today()

    workouts = Workout.objects.filter(date=today)
    meals = Meal.objects.filter(date=today)
    sleep = Sleep.objects.filter(date=today).last()

    total_workout = sum(w.duration for w in workouts)
    total_calories = sum(m.calories for m in meals)
    sleep_hours = sleep.hours if sleep else 0

    sleep_status = "Good Sleep ✅" if sleep_hours >= 6 else "Poor Sleep ❌"
    calorie_status = "Normal Intake ✅" if total_calories <= 2500 else "High Calories ⚠"
    workout_status = "Active 💪" if total_workout >= 20 else "Low Activity ⚠"

    overall = "Healthy Day ✅" if sleep_hours >= 6 and total_calories <= 2500 else "Needs Improvement ⚠"

    return render(request, 'summary.html', {
        "workout": total_workout,
        "calories": total_calories,
        "sleep": sleep_hours,
        "sleep_status": sleep_status,
        "calorie_status": calorie_status,
        "workout_status": workout_status,
        "overall": overall
    })

@csrf_exempt
def add_workout(request):
    data = json.loads(request.body)
    duration = int(data.get('duration', 0))

    # ✅ Save in Workout table
    Workout.objects.create(duration=duration)

    # ✅ Update HealthData aggregate
    obj, _ = HealthData.objects.get_or_create(id=1)
    obj.workout += duration
    obj.save()

    return JsonResponse({"status": "Workout saved"})

@csrf_exempt
def add_meal(request):
    data = json.loads(request.body)
    calories = int(data.get('calories', 0))

    Meal.objects.create(calories=calories)

    obj, _ = HealthData.objects.get_or_create(id=1)
    obj.calories += calories
    obj.save()

    return JsonResponse({"status": "Meal saved"})

@csrf_exempt
def add_sleep(request):
    data = json.loads(request.body)
    hours = float(data.get('hours', 0))

    Sleep.objects.create(hours=hours)

    obj, _ = HealthData.objects.get_or_create(id=1)
    obj.sleep += hours
    obj.save()

    return JsonResponse({"status": "Sleep saved"})