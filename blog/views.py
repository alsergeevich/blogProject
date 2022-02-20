from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from django.core.paginator import Paginator


class PostsHome(ListView):
    model = Posts
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True)


class PostsByCategory(ListView):
    model = Posts
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = Category.objects.get(slug=self.kwargs['cat_slug'])
        return context

    def get_queryset(self):
        return Posts.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class ShowPost(DetailView):
    model = Posts
    template_name = 'blog/view_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

