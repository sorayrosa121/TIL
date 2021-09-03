from django.db import models
# movies/models.py

from django.db import models

# Create your models here.
class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 방법1 ) 
    # 1번 영화: 영화제목
    def __str__(self):
        return f'{self.pk}번 영화: {self.title}'