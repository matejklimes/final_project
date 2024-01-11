# forms.py
from django import forms
from .models import Workout
from datetime import datetime

# forms.py
from django import forms

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'exercises']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the current time
        current_time = datetime.now().time()

        # Set default workout name based on the current time
        if current_time >= datetime.strptime('05:00:00', '%H:%M:%S').time() and current_time <= datetime.strptime('11:59:59', '%H:%M:%S').time():
            self.fields['name'].initial = 'Morning Workout'
        elif current_time >= datetime.strptime('12:00:00', '%H:%M:%S').time() and current_time <= datetime.strptime('17:59:59', '%H:%M:%S').time():
            self.fields['name'].initial = 'Afternoon Workout'
        elif current_time >= datetime.strptime('18:00:00', '%H:%M:%S').time() and current_time <= datetime.strptime('22:59:59', '%H:%M:%S').time():
            self.fields['name'].initial = 'Evening Workout'
        else:
            self.fields['name'].initial = 'Night Workout'



