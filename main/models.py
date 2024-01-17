from django.db import models
from django.contrib.auth.views import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='images', blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    views = models.IntegerField(default=0)
    video_url = models.FileField(upload_to='videos', blank=True, null=True)

    def __str__(self):
        return self.title

