from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Přidáno related_name pro zabránění konfliktu s vestavěnými modely
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username



class Exercises(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    CATEGORY_CHOICES = [
        ('barbell', 'Barbell'),
        ('dumbbell', 'Dumbbell'),
        ('machine', 'Machine / Other'),
        ('weighted_bw', 'Weighted Bodyweight'),
        ('assisted_bw', 'Assisted Bodyweight'),
        ('reps', 'Reps Only'),
        ('cardio', 'Cardio'),
        ('duration', 'Duration'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    BODYPART_CHOICES = [
        ('core', 'Core'),
        ('arms', 'Arms'),
        ('back', 'Back'),
        ('chest', 'Chest'),
        ('legs', 'Legs'),
        ('shoulders', 'Shoulders'),
        ('other', 'Other'),
        ('olympic', 'Olympic'),
        ('fullbody', 'Full Body'),
        ('cardio', 'Cardio'),
    ]
    bodypart = models.CharField(max_length=30, choices=BODYPART_CHOICES)

    def __str__(self):
        return self.name
    


class Workouts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField()
    duration = models.DurationField()
    note = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"



class ExercisesInWorkout(models.Model):
    id = models.BigAutoField(primary_key=True)
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE, related_name='exercises_in_workout')
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, related_name='workouts_for_exercise')
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.workout.user.username} - {self.workout.date} - {self.exercise.name}"
