from django.urls import path

from .views import index, exercise_list, ExerciseDetailView

urlpatterns = [
    path("", index, name="index"),
    path('exercises/', exercise_list, name='exercise_list'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
]

