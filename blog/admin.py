from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')  # поля которые будут отображаться
    list_display_links = ('id', 'title')  # поля которые будут ссылками
    search_fields = ('title', 'content')  # по каким полям будет осуществляться поиск
    list_editable = ('is_published',)  # редактируемое поле
    list_filter = ('is_published', 'time_create')  # список полей по которым мы сможем осуществлять фильтрацию
    # prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'time_create',  'is_published')
    list_display_links = ('id', 'content')
    list_filter = ('time_create', 'is_published')
    search_fields = ('id', 'content')
    readonly_fields = ('time_create',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'
