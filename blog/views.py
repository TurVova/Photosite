from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):

    model = Post
    template_name = 'blog/posts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_slug_field(self):
        return self.slug_field

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})
