from django.db import models

# Create your models here.
class Article(models.Model):
    # id 
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin 페이지에서 예쁘게 출력될 수 있도록
    def __str__(self):
        return f'{self.id}번 글 - {self.title} / {self.content}'