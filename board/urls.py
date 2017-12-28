from django.conf.urls import url

from .views import (
    BoardListView,
    BoardDetailView,
    BoardCreateView,
    BoardUpdateView,
    BoardDeleteView,
)

urlpatterns = [
    url(r'^check/(?P<check>\d+)/$', BoardListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',BoardDetailView.as_view(), name='detail'),
    url(r'^create/(?P<check>\d+)/$',BoardCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',BoardUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$',BoardDeleteView.as_view(), name='delete'),
]