from django.urls import path, include
from rest_framework.routers import DefaultRouter

from music.views import SongViewSet, AlbumViewSet, ArtistViewSet

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
router.register('artist', ArtistViewSet)


urlpatterns = [
    path('', include(router.urls)),
]