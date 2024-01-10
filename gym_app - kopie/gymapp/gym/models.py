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





