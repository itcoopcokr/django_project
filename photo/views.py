from django.shortcuts import render
from django.http import HttpResponse
import json

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

class PhotoAjaxDeleteView(DeleteView):
    model = Photo
    success_url = '/photo/'

    # allow delete only logged in user by appling decorator
    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # maybe do some checks here for permissions ...

        resp = super(PhotoAjaxDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"result": "ok"}
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")
        else:
            # POST request (not ajax) will do a redirect to success_url
            return resp
