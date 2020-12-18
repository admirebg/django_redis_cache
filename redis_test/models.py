from django.db import models
from django.core.cache import cache


class Post(models.Model):
    text = models.TextField()

    def save(self, *args, **kwargs):
        cache.delete('posts')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('posts')
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.text

