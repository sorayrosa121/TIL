# articles/models.py

from django.db import models

from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    image = models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/')
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title