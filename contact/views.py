from django.shortcuts import render

from django.views.generic import CreateView, TemplateView

from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'landingpage.html'
    success_url = '/contact/done'
    form_class = ContactForm

class ContactDoneView(TemplateView):
    template_name = 'contact_done.html'


