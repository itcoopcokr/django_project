from django.conf.urls import url

from .views import ContactCreateView, ContactDoneView

urlpatterns = [
    url(r'^create/$',ContactCreateView.as_view(), name='create'),
    url(r'^done/$',ContactDoneView.as_view(), name='done')
]