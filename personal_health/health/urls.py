from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('summary/', views.summary, name='summary'),
    path('summary-page/', views.summary_page),

    path('history/', views.history),

    path('health/', views.health),

    path('add-workout/', views.add_workout),
    path('add-meal/', views.add_meal),
    path('add-sleep/', views.add_sleep),
]