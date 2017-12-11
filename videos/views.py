from django.shortcuts import render

# Create your views here.
from .models import Video
from django.views.generic import ListView

class VideoListView(ListView):
    queryset = Video.objects.all()

    def get_context_data(self,*args, **kwargs):
        context = super(VideoListView,self).get_context_data(*args, **kwargs)
        return context
