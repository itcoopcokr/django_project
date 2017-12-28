from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

import json

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Board
from .forms import BoardForm
# Create your views here.

class BoardListView(ListView):
    model = Board
    template_name = 'board/board_list.html'
    paginate_by = 2

    def get_context_data(self, *args,  **kwargs):
        context = super(BoardListView, self).get_context_data(**kwargs)
        check = self.kwargs.get('check')
        context['object_list'] = Board.objects.filter(check = check)
        context['check'] = self.kwargs.get('check')
        return context


class BoardDetailView(DetailView):
    model = Board
    template_name = 'board/board_detail.html'

class BoardCreateView(CreateView):
    model = Board
    template_name = 'board/board_create.html'
    form_class = BoardForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(BoardCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BoardCreateView, self).get_context_data(**kwargs)
        context['check'] = self.kwargs['check']
        return context

class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_update.html'

class BoardDeleteView(DeleteView):
    model = Board
    template_name = 'board/board_delete_confirm.html'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = Board.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect(reverse('board:list', kwargs={'check': obj.check}))

