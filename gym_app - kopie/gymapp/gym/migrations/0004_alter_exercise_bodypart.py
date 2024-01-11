# Generated by Django 5.0 on 2024-01-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_alter_exercise_bodypart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='bodypart',
            field=models.CharField(choices=[('Core', 'Core'), ('Arms', 'Arms'), ('Back', 'Back'), ('Chest', 'Chest'), ('Legs', 'Legs'), ('Shoulders', 'Shoulders'), ('Other', 'Other'), ('Olympic', 'Olympic'), ('Full Body', 'Full body'), ('Cardio', 'Cardio')], max_length=30),
        ),
    ]