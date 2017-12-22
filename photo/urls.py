from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import url, static

from .views import (
    PhotoListView
)

urlpatterns = [
    url(r'^$', PhotoListView.as_view(), name='list'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)