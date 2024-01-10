from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Exercise



def index(request):
    return HttpResponse("Hello, world. You're at the gym index.")

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
    context_object_name = 'exercise'



