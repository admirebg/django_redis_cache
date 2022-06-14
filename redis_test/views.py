from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.core.cache import cache


def my_view(request):
    # cache.delete('posts')
    posts = cache.get('posts')
    if not posts:
        posts = list(Post.objects.filter(id__lte=10000).values('id', 'text'))
        cache.set('posts', posts)
    return JsonResponse(posts, safe=False)
