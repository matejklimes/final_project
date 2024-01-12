from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import DetailView, ListView, View
from django.db import transaction


from .models import Exercise, Workout, WorkoutExercise
from .forms import WorkoutForm



def index(request):
    return HttpResponse("Hello, world. You're at the gym index.")


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'
    context_object_name = 'exercises'


class ExerciseJSONView(View):
    def get(self, request, *args, **kwargs):
        exercises = Exercise.objects.all()
        data = list(exercises.values())
        return JsonResponse(data, safe=False)


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
    

class RunningWorkoutView(View):
    def get(self, request):
        form = WorkoutForm()
        return render(request, 'running_workout.html', {'form': form})

    def post(self, request):
        form = WorkoutForm(request.POST)
        if form.is_valid():
            # Save the workout without committing to the database
            workout = form.save(commit=False)

            # Save the workout to commit to the database and get an ID
            workout.save()

            # Retrieve the selected exercise IDs from the hidden input field
            selected_exercise_ids = request.POST.get('selected_exercises', '').split(',')
            selected_exercise_ids = [int(id) for id in selected_exercise_ids if id]

            # Associate the selected exercises with the workout
            workout.exercises.set(selected_exercise_ids)

            # Save the workout again to update the many-to-many relationship
            workout.save()

            # Redirect to the workout summary page with the newly created workout's ID
            return redirect('workout_summary', workout_id=workout.id)

        return render(request, 'running_workout.html', {'form': form})


class WorkoutSummaryView(View):
    def get(self, request, workout_id):
        workout = Workout.objects.get(pk=workout_id)
        return render(request, 'workout_summary.html', {'workout': workout})