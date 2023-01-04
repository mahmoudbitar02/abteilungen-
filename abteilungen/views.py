from django.shortcuts import render
from .models import abteilungen

# Create your views here.


from django.views.generic import ListView

class Postlist(ListView):
    model=abteilungen
