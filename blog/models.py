from django.db import models
from django.urls import reverse
from autoslug.fields import AutoSlugField


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = AutoSlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', populate_from='title')
    content = models.TextField(blank=True, verbose_name='Текст описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Каталог изделий'  # заменяем в админке название модели
        verbose_name_plural = 'Каталог изделий'  # определяем название во множественном числе
        ordering = ['time_create', 'title']  # определяем порядок сортировки


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'  # заменяем в админке название модели
        verbose_name_plural = 'Категории'  # определяем название во множественном числе
        ordering = ['id', ]  # определяем порялок сортировки


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments_posts', verbose_name='Описание',
                             blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    content = models.TextField(blank=True, verbose_name='Текст комментария')

    is_published = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        verbose_name = 'Комментарий'  # заменяем в админке название модели
        verbose_name_plural = 'Комментарии'  # определяем название во множественном числе
        ordering = ['time_create', ]  # определяем порялок сортировки


class My_Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = AutoSlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', populate_from='title')
    content = models.TextField(blank=True, verbose_name='Текст описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')
    email = models.CharField(max_length=255, verbose_name='Email')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Обо мне'  # заменяем в админке название модели
        verbose_name_plural = 'Обо мне'  # определяем название во множественном числе
        ordering = ['time_create', 'title']  # определяем порядок сортировки

