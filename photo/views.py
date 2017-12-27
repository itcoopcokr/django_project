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
    paginate_by = 2


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()

        return super(PhotoCreateView, self).form_valid(form)

class PhotoUpdateView(UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_update.html'

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete_confirm.html'
    success_url = '/photo/'
