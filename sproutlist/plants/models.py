from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    watering_interval = models.IntegerField(help_text="Days between watering")
    last_watered = models.DateField(auto_now_add=True) 
    fertilization_interval = models.IntegerField(help_text="Days between fertilization")
    last_fertilized = models.DateField(auto_now_add=True)

class ToDo(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20, choices=[('WATER', 'Water'), ('FERTILIZE', 'Fertilize')])
    due_date = models.DateField()
    completed = models.BooleanField(default=False)