from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.core.cache import cache


def my_view(request):
    # posts = Post.objects.filter(id__lte=10000).values('id', 'text')
    posts = cache.get_or_set('posts', Post.objects.filter(id__lte=10000).values('id', 'text'))
    return JsonResponse(list(posts), safe=False)
