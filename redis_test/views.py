from django.shortcuts import render
from django.http import JsonResponse
from .models import Post


def my_view(request):
    posts = Post.objects.filter(id__lte=10000).values('id', 'text')
    return JsonResponse(list(posts), safe=False)
