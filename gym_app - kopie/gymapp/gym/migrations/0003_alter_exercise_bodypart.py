# Generated by Django 5.0 on 2024-01-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_rename_exercises_exercise_rename_workouts_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='bodypart',
            field=models.CharField(choices=[('Core', 'core'), ('Arms', 'arms'), ('Back', 'back'), ('Chest', 'chest'), ('Legs', 'legs'), ('Shoulders', 'shoulders'), ('Other', 'other'), ('Olympic', 'olympic'), ('Full Body', 'fullbody'), ('Cardio', 'cardio')], max_length=30),
        ),
    ]
