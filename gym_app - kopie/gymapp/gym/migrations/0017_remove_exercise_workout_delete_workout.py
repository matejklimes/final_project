# Generated by Django 5.0 on 2024-01-10 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0016_remove_workout_end_time_remove_workout_start_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
