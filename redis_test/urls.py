from django.urls import path

from .views import my_view


urlpatterns = [
    path('redis_test/', my_view),
]