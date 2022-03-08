from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostsByCategory.as_view(), name='category'),
    path('zakaz/', ContactFormView.as_view(), name='zakaz')


]
