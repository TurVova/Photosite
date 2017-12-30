from django.shortcuts import render
from django.views.generic import TemplateView
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

def custom_404(request):
    return render(request, '404.html')

def custom_500(request):
    return render(request, '500.html')