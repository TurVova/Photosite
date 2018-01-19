from django.views.generic import TemplateView
from django.shortcuts import render
from gallery_app.models import Album, Photo


class AlbumView(TemplateView):
    template_name = 'gallery/album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album_list'] = Album.objects.all()

        return context


class PhotoView(TemplateView):
    template_name = 'gallery/photo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.all()

        return context

def album_list(request):
    albums = Album.objects.all()
    for album in albums:
        photos = Album.objects.get(name=album).photo_set.all()

    return render(request, 'gallery/photo_list.html', {'ob_list' : photos})
