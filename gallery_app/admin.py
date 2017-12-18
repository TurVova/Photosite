from django.contrib import admin

from gallery_app.models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']

    class Meta:
        model = Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']

    class Meta:
        model = Photo


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
