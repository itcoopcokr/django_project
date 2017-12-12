from django.shortcuts import render

# Create your views here.
from .models import Video
from django.views.generic import ListView
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import VideoForm

class VideoListView(ListView):
    queryset = Video.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(VideoListView,self).get_context_data(*args, **kwargs)
        context['all_count'] = Video.objects.all().count()
        return context

class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
        return context

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm

class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'
