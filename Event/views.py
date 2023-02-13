from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from .models import Event
# Create your views here.


def index(self):
    return HttpResponse("Bonjour 4TWIN2")


def affiche(request):
    events = Event.objects.all()
    return render(request, "Event/affiche.html", {"events": events})
=======

# Create your views here.
>>>>>>> 3ed9813b3c5878d7b5d3f7df95dcb9e91e62ae72
