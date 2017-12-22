from django.db import models
from .fields import ThumbnailImageField

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=120)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title
