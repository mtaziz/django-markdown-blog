from django.views.generic import DetailView, ListView

from .models import Page, Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.published()

    def get_queryset(self):
        qs = super().get_queryset()
        if 'tag' in self.kwargs:
            qs = qs.filter(tags__slug__in=[self.kwargs['tag']])
        return qs


class PostDetail(DetailView):
    model = Post


class PageDetail(DetailView):
    model = Page
