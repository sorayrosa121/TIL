from django.contrib import admin
from .models import Article

# Register your models here.

# 기본적으로 사용자가 입력한 부분만 admin페이지에서 조회할 수 있기때문에,
# 생성일자는 추가적으로 조회할 수 있도록 하단 수정
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')


# 위에서 생성한 ArticleAdmin도 추가
admin.site.register(Article, ArticleAdmin)