from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Plant, ToDo
from .forms import PlantForm 


# Create your views here.

def plant_list(request):
    plants = Plant.objects.all()
    todos = ToDo.objects.filter(completed=False)
    return render(request, 'plants/plant_list.html', {'plants': plants, 'todos': todos})

def add_plant(request):
    if request.method == 'POST':  
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('plant_list')  
    else: 
        form = PlantForm() 
    return render(request, 'plants/add_plant.html', {'form': form})