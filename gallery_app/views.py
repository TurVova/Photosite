from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, redirect
from gallery_app.models import Album, Photo


class AlbumsView(TemplateView):
    template_name = 'gallery/album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album_list'] = Album.objects.all()

        return context


class PhotosView(TemplateView):
    template_name = 'gallery/photo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.all()

        return context

def get_album(request, album_slug):
    albums = Album.objects.all()
    get_slug = Album.objects.get(slug=album_slug)
    context = {
        'albums' : albums,
        'get_slug' : get_slug,
    }

    return render(request, 'gallery/photo_list.html', context)
