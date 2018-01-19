from django.urls import path
from django.conf.urls.static import static

from photosite import settings
from gallery_app.views import AlbumView, PhotoView
from . import views


urlpatterns = [
        path('', AlbumView.as_view(), name='album'),
        path('photos/', PhotoView.as_view(), name='photo'),
        path('all/', views.album_list, name='ob_list')
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
