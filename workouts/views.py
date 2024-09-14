from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise, WorkoutExercise
from .forms import WorkoutForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'notes']

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight']

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'workouts/add_workout.html', {'form': form})

@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id, user=request.user)
    exercises = WorkoutExercise.objects.filter(workout=workout)
    
    if request.method == 'POST':
        form = WorkoutExerciseForm(request.POST)
        if form.is_valid():
            workout_exercise = form.save(commit=False)
            workout_exercise.workout = workout
            workout_exercise.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutExerciseForm()
    
    return render(request, 'workouts/workout_detail.html', {
        'workout': workout,
        'exercises': exercises,
        'form': form
    })

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'workouts/add_workout.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
