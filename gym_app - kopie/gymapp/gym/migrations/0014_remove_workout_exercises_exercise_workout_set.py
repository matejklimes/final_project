# Generated by Django 5.0 on 2024-01-10 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0013_workoutexerciseset_workoutexercise_workout_sets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='exercises',
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='gym.workout'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('reps', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='gym.exercise')),
            ],
        ),
    ]
