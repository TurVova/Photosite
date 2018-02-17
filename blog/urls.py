from django.urls import path
from blog.views import PostListView, PostDetail

# app_name = 'blog'

urlpatterns = [
    path('blog/', PostListView.as_view(), name='posts_list'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='posts_detail'),
]