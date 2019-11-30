from django.db import models
from embed_video.fields import EmbedVideoField

class Wedding(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    video = EmbedVideoField(blank=True, verbose_name='Видео')



class Film(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    video = EmbedVideoField(blank=True, verbose_name='Видео')