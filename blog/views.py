from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.views.generic.edit import FormMixin
from django.contrib import messages


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


class ShowPost(FormMixin, DetailView):
    model = Posts
    template_name = 'blog/view_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан, ожидайте модерации'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'post_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, self.success_msg)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'blog/zakazform.html'
    success_url = reverse_lazy('zakaz')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Форма заказа'
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        content = form.cleaned_data['content']
        send_mail(f'Заказ от {name}', content + f' \nEmail заказчика {from_email}', settings.EMAIL_HOST_USER, ['yuliazaskotchenko@yandex.ru'])
        return redirect('zakaz')
