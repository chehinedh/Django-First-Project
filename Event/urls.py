<<<<<<< HEAD
from django.urls import path, include
from .views import index, affiche
urlpatterns = [
    path('', index),
    path('all/', affiche),
=======
from django.urls import render
from . import views

urlpatterns = [
    path('index/', index.views),
    path('afficher/',views.affiche)
>>>>>>> 382a5b1c5fe03e9e5ad661295f04e4da1a45e154
]