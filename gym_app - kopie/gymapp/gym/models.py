from django.db import models



class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField()
    CATEGORY_CHOICES = [
        ('Barbell', 'barbell'),
        ('Dumbbell', 'dumbbell'),
        ('Machine / Other', 'machine'),
        ('Weighted Bodyweight', 'weighted_bw'),
        ('Assisted Bodyweight', 'assisted_bw'),
        ('Reps Only', 'reps'),
        ('Cardio', 'cardio'),
        ('Duration', 'duration'),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    BODYPART_CHOICES = [
        ('Core', 'core'),
        ('Arms', 'arms'),
        ('Back', 'back'),
        ('Chest', 'chest'),
        ('Legs', 'legs'),
        ('Shoulders', 'shoulders'),
        ('Other', 'other'),
        ('Olympic', 'olympic'),
        ('Full Body', 'fullbody'),
        ('Cardio', 'cardio'),
    ]
    bodypart = models.CharField(max_length=30, choices=BODYPART_CHOICES)

    def __str__(self):
        return self.name
    


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='sets')
    reps = models.PositiveIntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"Set for {self.exercise.name}"



class WorkoutExercise(models.Model):
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.ManyToManyField(Set, blank=True)

    def __str__(self):
        return f"WorkoutExercise for {self.workout} - {self.exercise}"
    


class Workout(models.Model):
    name = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise, through=WorkoutExercise, blank=True)

    def __str__(self):
        return self.name if self.name else f'Workout {self.pk}'






