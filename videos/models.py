from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=120)
    embed_code = models.TextField()

    def __str__(self):
        return str(self.title)
