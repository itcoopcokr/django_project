"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import Home, Base, Team, Landingpage
from videos.views import VideoListView
from videos.views import (
    VideoDetailView,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView
)

from .views import UserCreateView, UserCreateDoneView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'accounts/register/done/$', UserCreateDoneView.as_view(), name='register_done'),
    url(r'^$', Home.as_view()),
    url(r'^base/$', Base.as_view()),
    url(r'^team/$', Team.as_view()),
    url(r'^index/$', Landingpage.as_view()),
    url(r'^videos/$', VideoListView.as_view(), name='videos'),
    url(r'^videos/(?P<pk>\d+)/$',VideoDetailView.as_view(), name='video-detail'),
    url(r'^videos/create/$', VideoCreateView.as_view(), name='video-create'),
    url(r'^videos/(?P<pk>\d+)/update/$', VideoUpdateView.as_view(), name='video-update' ),
    url(r'^videos/(?P<pk>\d+)/delete/$', VideoDeleteView.as_view(), name='video-delete' )


]
