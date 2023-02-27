from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.
<<<<<<< HEAD
def index(self):
    return HttpResponse("Morning")
def affiche(request):
    events = Event.objects.all()
    return render(request,"Event/affiche.html", {"events":events})
=======


def index(self):
    return HttpResponse("Bonjour 4TWIN2")


def affiche(request):
    events = Event.objects.all()
    return render(request, "Event/affiche.html", {"events": events})
>>>>>>> 9df20a278344971af19dd09cacff2d5464ee3c0c
