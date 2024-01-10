from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, View

from .models import Exercise, Workout



def index(request):
    return HttpResponse("Hello, world. You're at the gym index.")

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
    context_object_name = 'exercise'

class WorkoutListView(ListView):
    model = Workout
    template_name = 'workout_list.html'
    context_object_name = 'workouts'
    ordering = ['-date_created']

class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'workout_detail.html'
    context_object_name = 'workout'

class StartNewWorkoutView(View):
    def get(self, request, *args, **kwargs):
        # Add any logic for starting a new workout (e.g., creating a new workout instance)
        # For now, let's redirect to a placeholder template "running_workout.html"
        return redirect('running_workout')



