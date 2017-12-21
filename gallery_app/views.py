from django.views.generic import TemplateView
from gallery_app.models import Album, Photo


class AlbumView(TemplateView):
    template_name = 'gallery/album.html'

    def get_context_data(self, **kwargs):
        album_list = Album.objects.all()
        context = {
                'albums': album_list,
            }
        return context


class PhotoView(TemplateView):
    template_name = 'gallery/photo.html'

    def get_context_data(self, **kwargs):
        photo_list = Photo.objects.all()
        context = {
                'photos': photo_list,
            }
        return context
