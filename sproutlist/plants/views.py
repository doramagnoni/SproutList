from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Plant, ToDo

def plant_list(request):
    plants = Plant.objects.all()
    todos = ToDo.objects.filter(completed=False)
    return render(request, 'plants/plant_list.html', {'plants': plants, 'todos': todos})