[TOC]


# 작성과정
<br>

## 01. URL

```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include               # include 추가 import

urlpatterns = [
    path('articles/', include('articles.urls')),    # http://127.0.0.1:8000/articles/
    path('admin/', admin.site.urls),
]
```

- `include`를 추가로 import
- `crud/urls.py`에 `articles`를 추가함으로써,  `http://127.0.0.1:8000/articles/`를 기본 주소로 가질 수 있도록 작성

<br>

```python
# articles/urls.py

from django.urls import path
from . import views                                 # articles/views.py에 작성한 내용들

app_name = 'articles'                               # app이름
urlpatterns = [
    path('', views.index, name='index'),            # name으로 입력한 값은 form태그 사용 시, <app_name>:<url_name>으로 사용
    path('create/', views.create, name='create'),   # {% url 'articles:create' %}
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),        
]
```
<br>

## 02. MODEL

```python
# articles/models.py

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):      # Article object(1), Article object(2)가 아닌 제목으로 표시됨
        return self.title
```

<br>

## 03. FORM

```python
# articles/forms.py

from django import forms
from .models import Article # articles/modesl.py 에서 작성한 Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['title', 'content']
        # fields = ('title', 'content')
        # exclude = ('title',) # 제외할 필드. 튜플 형태로 사용하기 위해 콤마',' 작성
```

<br>

## 04. VIEW

```python
# articles/views.py

from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article             # articles/models.py 에서 작성한 Article
from .forms import ArticleForm          # articles/forms.py 에서 작성한 ArticleForm

# Create your views here.
@require_safe                           # view가 GET 및 HEAD 메서드만 허용하도록 제한하는 데코레이터
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(["GET", "POST"])  # view 가 특정 요청만 허용하도록 제한하는 데코레이터
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# @require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

```

<br>

## 05. TEMPLATE

```django
<!-- templates/base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1>CRUD with ModelForm</h1>
        <hr>
        {% block content %}    
        {% endblock content %}
    </div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```

- Bootstrap CDN 추가

<br>

```python
# crud/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # BASE_DIR 추가 작성
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- `crud/settings.py` 의 `TEMPLATES`에서 `BASE_DIR/'templates'`를 추가

<br>


# 결과물

<br>

## 01. Read

![image-20210907163819286](0907_workshop.assets/image-20210907163819286.png)

<br>

```django
<!-- articles/templates/articles/index.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Articles</h2>
    <a href="{% url 'articles:create' %}"class='text-decoration-none'>NEW</a>
    <hr>
    {% for article in articles %}
        <h3>{{ article.pk}}</h3>
        <h3>{{ article.title}}</h3>
        <a href="{% url 'articles:detail' article.pk%}" class="text-decoration-none" >DETAIL</a>
        <hr>
    {% endfor %}
{% endblock content %}
```

<br>

## 02. Create

![image-20210907164336648](0907_workshop.assets/image-20210907164336648.png)

<br>

```django
<!-- articles/templates/articles/create.html -->

{% extends 'base.html' %}

{% block content %}
  <h2>New</h2>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p}}
    <input type="submit" value="submit">
  </form>
  <a href="{% url 'articles:index' %}" class='text-decoration-none'>BACK</a>
{% endblock content %}
```



<br>

## 03. Detail

![image-20210907164503741](0907_workshop.assets/image-20210907164503741.png)

<br>

```django
<!-- articles/templates/articles/detail.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Detail</h2>
    <hr>
    <h3>글 번호: {{article.pk }}</h3>
    <h3>글 제목: {{article.title }}</h3>
    <p>글 내용: {{ article.content }}</p>
    <p>글 생성시각: {{ article.created_at }}</p>
    <p>글 수정시각: {{ article.updated_at }}</p>
    
    <form action="{% url 'articles:update' article.pk%}" method='GET'>
        <input type="submit" value="EDIT" style="color: blue;" class="bg-white border border-white text-start">
    </form>
    <form action="{% url 'articles:delete' article.pk%}" method='POST'>
        {% csrf_token %}
        <input type="submit" value="DELETE" style="color: blue;" class="bg-white border border-white text-start">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}" class="text-decoration-none">BACK</a>
{% endblock content %}
```

<br>

## 04. Update

![image-20210907164848784](0907_workshop.assets/image-20210907164848784.png)

<br>

```django
<!-- articles/templates/articles/update.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>Edit</h2>
    <form action="{% url 'articles:update' article.pk%}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="submit">
    </form>
    <a href="{% url 'articles:detail' article.pk%}" class="text-decoration-none">BACK</a>

{% endblock content %}
```

<br>

## 05. Read

![image-20210907164955332](0907_workshop.assets/image-20210907164955332.png)

<br>

## 06. Delete

![image-20210907181753668](0907_workshop.assets/image-20210907181753668.png)

<br>

