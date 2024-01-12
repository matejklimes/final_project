import os
import django
import json

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymapp.settings')  # Replace 'your_project' with your actual Django project name
django.setup()

from gym.models import Exercise  # Replace 'your_app' with the actual name of your Django app

def add_exercises_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for exercise_data in data:
        exercise = Exercise(
            name=exercise_data['name'],
            description=exercise_data['description'],
            category=exercise_data['category'],
            bodypart=exercise_data['bodypart']
        )
        exercise.save()

if __name__ == '__main__':
    json_file_path = 'exported_exercises.json'  # Replace with the actual path to your JSON file
    add_exercises_from_json(json_file_path)
