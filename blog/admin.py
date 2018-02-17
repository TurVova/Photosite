from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post

        
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'user', 'create']
    date_hierarchy = 'create'
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15
    summernote_fields = ('text',)

    class Meta:
        model = Post
        
# admin.site.register(User, UserAdmin)
# admin.site.register(Post, PostAdmin)