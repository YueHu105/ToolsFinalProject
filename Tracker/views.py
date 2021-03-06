from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Squirrels
import json
from django.db.models import Avg, Max, Min, Count
# Create your views here.

def leafletmap(request):
    squirrel_list = Squirrels.objects.all()[0:100]
    sqList = [{"Y": float(sq.Longitude), "X": float(sq.Latitude), "ID": sq.Unique_Squirrel_ID} for sq in squirrel_list]
    context = {'squirrel_list': json.dumps(sqList)}
    return render(request, 'Tracker/map.html', context)

class SquirrelList(ListView):
    model = Squirrels
    template_name = 'Tracker/squirrels_list.html'

class SquirrelUpdate(UpdateView):
    model = Squirrels
    fields = ["Latitude", "Longitude", "Unique_Squirrel_ID", "Shift", "Date", "Age", "Primary_Fur_Color", "Location", "Specific_Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other_Activities", "Kuks", "Quaas", "Moans", "Tail_flags", "Tail_twitches", "Approaches", "Indifferent", "Runs_from"]
    success_url = reverse_lazy('squirrel_list')
    template_name = 'Tracker/squirrels_form.html'

class SquirrelAdd(CreateView):
    model = Squirrels
    fields = ["Latitude", "Longitude", "Unique_Squirrel_ID", "Shift", "Date", "Age", "Primary_Fur_Color", "Location", "Specific_Location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other_Activities", "Kuks", "Quaas", "Moans", "Tail_flags", "Tail_twitches", "Approaches", "Indifferent", "Runs_from"]
    success_url = reverse_lazy('squirrel_list')
    template_name = 'Tracker/squirrels_add.html'

class SquirrelStats(ListView):
    model = Squirrels
    template_name = "Tracker/squirrels_stats.html"

def stats(request):
    squirrel_list = Squirrels.objects.all()
    a = len(squirrel_list)
    b = squirrel_list.aggregate(average_longitude=Avg('Longitude'))
    c = squirrel_list.aggregate(min_latitude=Min('Latitude'), max_latitude=Max('Latitude'))
    d = list(squirrel_list.values_list('Location').annotate(Count('Location')))
    e = list(squirrel_list.values_list('Shift').annotate(Count('Shift')))
    return render(request, 'Tracker/squirrels_stats.html', {"a": a, "b": b, "c": c, "d": d, "e": e, })
