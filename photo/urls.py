from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import url, static

from .views import (
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
)

urlpatterns = [
    url(r'^$', PhotoListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',PhotoDetailView.as_view(), name='detail'),
    url(r'^create/$',PhotoCreateView.as_view(), name='create'),

]