# forms.py
from django import forms
from .models import Workout

# forms.py
from django import forms

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'exercises']



