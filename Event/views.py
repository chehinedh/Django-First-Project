from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.


def index(self):
    return HttpResponse("Bonjour 4TWIN2")


def affiche(request):
    events = Event.objects.all()
    return render(request, "Event/affiche.html", {"events": events})
