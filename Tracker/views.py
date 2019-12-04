from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Squirrels
import json
# Create your views here.

def leafletmap(request):
    squirrel_list = Squirrels.objects.all()[0:100]
    sqList = [{"X": float(sq.Longitude), "Y": float(sq.Latitude), "ID": sq.Unique_Squirrel_ID} for sq in squirrel_list]
    context = {'squirrel_list': json.dumps(sqList)}
    return render(request, 'Tracker/map.html', context)


class SquirrelList(ListView):
    model = Squirrels

class SquirrelUpdate(UpdateView):
    model = Squirrels
    fields = ["Latitude", "Longitude", "Primary_Fur_Color"]
    success_url = reverse_lazy('squirrel_list')


class SquirrelDelete(DeleteView):
    model = Squirrels
    success_url = reverse_lazy('squirrel_list')

class SquirrelAdd(CreateView):
    model = Squirrels
    fields = ["Latitude", "Longitude", "Unique_Squirrel_ID", "Shift", "Date", "Age", "Primary_Fur_Color", "Location", "Specific_Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other_Activities", "Kuks", "Quaas", "Moans", "Tail_flags", "Tail_twitches", "Approaches", "Indifferent", "Runs_from"]
    success_url = reverse_lazy('squirrel_list')

class SquirrelStats(ListView):
    model = Squirrels
    template_name = "Tracker/squirrels_stats.html"