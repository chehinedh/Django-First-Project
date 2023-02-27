from django.shortcuts import render
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
from django.http import HttpResponse
from .models import Event
# Create your views here.
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a


def index(self):
    return HttpResponse("Bonjour 4TWIN2")


def affiche(request):
    events = Event.objects.all()
    return render(request, "Event/affiche.html", {"events": events})
<<<<<<< HEAD
>>>>>>> 9df20a278344971af19dd09cacff2d5464ee3c0c
=======
=======

# Create your views here.
>>>>>>> 3ed9813b3c5878d7b5d3f7df95dcb9e91e62ae72
>>>>>>> 3ab9d94c055339275ba825dfc462c43b16398c1a
