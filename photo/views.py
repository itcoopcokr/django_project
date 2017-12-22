from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .models import Photo
# Create your views here.

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

