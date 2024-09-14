from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('add/', views.add_workout, name='add_workout'),
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
]