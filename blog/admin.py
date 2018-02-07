from django.contrib import admin

from blog.models import User, Post

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'create']
    date_hierarchy = 'create'
    list_per_page = 15
    
    class Meta:
        model = User
        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'create']
    date_hierarchy = 'create'
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15

    class Meta:
        model = Post
        
# admin.site.register(User, UserAdmin)
# admin.site.register(Post, PostAdmin)