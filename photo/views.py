from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Photo
from .forms import PhotoForm
# Create your views here.

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm


