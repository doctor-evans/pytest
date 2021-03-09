from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('songs', views.SongView)
router.register('audiobook', views.AudiobookView)
router.register('podcast', views.PodcastView)


urlpatterns = [
    path('testapi/',include(router.urls))
]
