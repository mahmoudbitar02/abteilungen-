from django.shortcuts import render
from .models import abteilungen

# Create your views here.


from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

class Postlist(ListView):
    model=abteilungen


class Postdetail(DetailView):
    model = abteilungen
    

class PostCreate(CreateView):  
    model=abteilungen
    fields = ['titel', 'content', 'image']  
    success_url = '/blog/'


class PostUpdate(UpdateView):  
    model=abteilungen
    fields = ['titel', 'content', 'image']  
    success_url = '/blog/'
