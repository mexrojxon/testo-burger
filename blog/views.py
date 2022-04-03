from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, reverse, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView
from taggit.models import Tag
from .form import CommentModelForm
from .models import BlogPostModel, CommentModel
from .form import CommentModelForm


class BlogListView(ListView):
    template_name = 'main/blog.html'
    queryset = BlogPostModel.objects.order_by('-pk')
    model = BlogPostModel
    context_object_name = 'posts'
    paginate_by = 3


class TagIndexView(ListView):
    model = BlogPostModel
    template_name = 'main/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPostModel.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'


class BlogCommentView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(BlogPostModel, pk=self.kwargs.get('pk'))
        return super(BlogCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs.get('pk')})
