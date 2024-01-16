from django.db import models
from django.contrib.auth.views import get_user_model

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='images')
    author = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    video_url = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title

