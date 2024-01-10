from django.urls import path

from .views import index, ExerciseListView, ExerciseDetailView, WorkoutListView, WorkoutDetailView, StartNewWorkoutView

urlpatterns = [
    path("", index, name="index"),
    path('exercises/', ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('workouts/', WorkoutListView.as_view(), name='workout_list'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout_detail'),  # Use the class-based view
    path('start_new_workout/', StartNewWorkoutView.as_view(), name='start_new_workout'),  # Use as_view() here
]

