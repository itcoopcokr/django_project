from django.shortcuts import render

# Create your views here.
from .models import Video
from django.views.generic import ListView
from django.views.generic import DetailView

class VideoListView(ListView):
    queryset = Video.objects.all()
    all_count = Video.objects.all().count()
    print("all_count=",all_count)

    def get_context_data(self,*args, **kwargs):
        context = super(VideoListView,self).get_context_data(*args, **kwargs)
        context['count'] = 4
        context['all_count'] = self.all_count
        return context

class VideoDetailView(DetailView):
    queryset = Video.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
        return context