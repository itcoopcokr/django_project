from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import url, static

from .views import (
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    PhotoAjaxDeleteView,
)

urlpatterns = [
    url(r'^', PhotoListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',PhotoDetailView.as_view(), name='detail'),
    url(r'^create/$',PhotoCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$',PhotoUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$',PhotoDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/delete_ajax/$',PhotoAjaxDeleteView.as_view(), name='delete_ajax'),
]