from django.contrib import admin
from .models import Exercise, Workout, Set, WorkoutExercise

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
admin.site.register(Set)
