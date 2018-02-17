from django.urls import path

from gallery_app.views import PhotosView, AlbumsView
from . import views


urlpatterns = [
        path('albums/', AlbumsView.as_view(), name='albums'),
        path('photos/', PhotosView.as_view(), name='photos'),
        path('album/<slug:album_slug>/', views.get_album, name='album_photo'),
    ]

