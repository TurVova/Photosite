from django.contrib import admin

from gallery_app.models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']
    date_hierarchy = 'create'
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Album

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'album', 'create']
    radio_fields = {'album': admin.HORIZONTAL}
    date_hierarchy = 'create'
    list_per_page = 15

    class Meta:
        model = Photo


# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Photo, PhotoAdmin)
