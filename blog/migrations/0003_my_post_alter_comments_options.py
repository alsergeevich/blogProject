# Generated by Django 4.0.1 on 2022-03-13 07:44

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title', unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Текст описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['time_create'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
