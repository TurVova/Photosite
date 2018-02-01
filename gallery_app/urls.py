from django.urls import path
from django.conf.urls.static import static

from photosite import settings
from gallery_app.views import PhotosView, AlbumsView
from . import views


urlpatterns = [
        path('albums/', AlbumsView.as_view(), name='albums'),
        path('photos/', PhotosView.as_view(), name='photos'),
        path('album/<slug:album_slug>/', views.get_album, name='album_photo'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
