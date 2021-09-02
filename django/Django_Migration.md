### 설치 및 가상환경 설정



1. 새로운 프로젝트 폴더 `Django_project`를 만들고 vscode로 열기

2. `venv`라는 이름의 가상환경 생성

   `python -m venv venv`

3. 가상환경 활성화

   `source venv/Scripts/activate`

4. pip 설치 리스트를 확인하여, 새로운 가상환경이 정상적으로 작동 중인지 확인

   `pip list`

5. Django 설치

   `pip install django`

6. `.gitignore` [내용 복붙]((https://www.toptal.com/developers/gitignore/api/python,visualstudiocode,django,venv)) 후, 파일 생성

7. 가상환경에 설치한 pip 목록을 `requirements.txt` 파일에 저장 (향후 git hub 등으로 공유 가능)

   `pip freeze > requirements.txt`

8. `config`라는 이름의 프로젝트 생성 (끝에 '.' 을 작성하지 않으면 config/config와 같이 하위폴더에 생성됨)

   `django-admin startproject config .`

9. Django가 정상적으로 작동하는지 확인 (bash에 뜨는 `http://127.0.0.1:8000/` 클릭, 혹은 주소 입력)

   `python manage.py runserver`

10. 서버가 정상적으로 작동하면 `Ctrl + c`로 서버를 멈춘 후, `articles`라는 이름의 app 생성

    `python manage.py startapp articles`

11. ★중요) `config`폴더의 `settings.py` -> `INSTALLED_APPS`에 articles app추가

    ```python
    INSTALLED_APPS = [
        'articles',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

12. `settings.py`에서 `LANGUAGE_CODE`를 `ko-kr`로 변경 후 저장, `8.` 번으로 서버를 다시 실행하면 한국어로 설정 가능

     `LANGUAGE_CODE = 'ko-kr'`

     `TIME_ZONE = 'Asia/Seoul'`



### URL_경로생성 및 최초페이지



1. `config` > `urls.py`파일에 `include`를 추가로 import하고, `urlpatterns` 부분을 수정

   ```python
   """config URL Configuration
   
   The `urlpatterns` list routes URLs to views. For more information please see:
       https://docs.djangoproject.com/en/3.2/topics/http/urls/
   Examples:
   Function views
       1. Add an import:  from my_app import views
       2. Add a URL to urlpatterns:  path('', views.home, name='home')
   Class-based views
       1. Add an import:  from other_app.views import Home
       2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
   Including another URLconf
       1. Import the include() function: from django.urls import include, path
       2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
   """
   from django.contrib import admin
   from django.urls import path, include   # include 추가로 import
   
   urlpatterns = [
       #  새로 생성할 articles/urls.py에 대한 경로 지정
       path('articles/', include('articles.urls')),
   
       path('admin/', admin.site.urls),
   ]
   ```

   

2. `articles` 폴더에 `urls.py` 파일 생성

   ```python
   # articles/urls.py
   # config/urls.py와 연결됨
   
   from django.urls import path
   
   # articles 폴더(.) 안에 있는 view.py를 import
   from . import views
   
   # app 이름 설정 (나중에 'articles:index'처럼 앱 이름으로 사용 가능)
   app_name = 'articles'
   
   urlpatterns = [
       path('index/', views.index, name='index'),
       path('', views.index),  # 기본주소 http://127.0.0.1:8000/articles
   ]
   ```

 

### VIEW_경로생성 및 최초페이지



1. `views.py`에 `index` view 관련 내용 추가

   ```python
   from django.shortcuts import render
   
   # Create your views here.
   def index(request):
       return render(request, 'articles/index.html')	# 하단 TEMPLATE에서 index.html 생성
   ```

### 

### TEMPLATE_경로생성 및 최초페이지



1. `Django_project`에 `templates` 디렉토리(폴더) 생성

2. `templates` 폴더에 `base.html` 파일 생성 (bootstrap CDN, div.container 내부에 block 추가)

   ```django
   <!-- base.html -->
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
       {% comment %} https://getbootstrap.com/docs/5.0/getting-started/introduction/ {% endcomment %}
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
   </head>
   <body>
       {% comment %} div.container 생성 후 {% endcomment %}
       <div class="container">
           {% block content %}
           {% comment %} content 라는 이름의 block을 통해, 
           다른 html에서 base.html을 extends할 수 있도록 작성 {% endcomment %}
           {% endblock content %}
       </div>
   
   {% comment %} bootstrap {% endcomment %}
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   

3. `settings.py` 파일 `TEMPLATES`의 `DIRS`에 해당 내용 추가

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           
           # templates 경로 설정 필요
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

    

4. `articles` 디렉토리에 `templates 폴더` 생성 후, 또다시 `articles 폴더`를 생성

5. `articles/templates/articles/` 경로에 `index.html` 파일 생성

   ```django
   <!-- articles/index.html -->>
   
   {% extends 'base.html' %}
   {% comment %} base.html의 내용을 이어서 받아옴 {% endcomment %}
   
   {% block content %}
       <h1>INDEX</h1>
       <hr>
       <p>제목: </p>
       <p>내용: </p>
   {% endblock content %}
   ```

6. template 수정 후에는 `Ctrl + c`로 서버를 중단한 후, 재 시작하여 반영시킴

   `python manage.py runserver`

   

### MODEL



1. `articles` 폴더의 `models.py` 파일에 `Article` 클래스 내용 추가

   ```python
   # articles/models.py
   
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       # id(PK, primary key) 자동 생성
       # makemigrations 후 생성되는 migrations/0001_initial.py 파일에서 확인 가능
       
       title = models.CharField(max_length=10) # 제목의 데이터 타입 CharField()는 글자 수 제한 필요(max_length가 필수 인자) 
       content = models.TextField()            # 글자 수 제한 없음
   ```

   

2. `models.py`의 수정사항에 기반한 새로운 마이그레이션(설계도) 생성 (articles/migrations/0001_initial.py가 생성됨)

   `$ python manage.py makemigrations`

3. `migrate`하기(makemigrations한 내용을 기반으로 동기화)

   `python manage.py migrate`

4. `models.py`에 `created_at`, `updated_at`이라는 내용 추가 작성

   ```python
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       # id(PK, primary key) 자동 생성
       # makemigrations 후 생성되는 migrations/0001_initial.py 파일에서 확인 가능
       
       title = models.CharField(max_length=10) # 제목의 데이터 타입 CharField()는 글자 수 제한 필요(max_length가 필수 인자) 
       content = models.TextField()            # 글자 수 제한 없음
       
   
       # 새롭게 마이그레이션 생성하면, 0002에 추가될 내용
       created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add: 최초 생성일자에'만' 현재 날짜/시간으로 갱신
       updated_at = models.DateTimeField(auto_now=True)        # auto_now: 최종 수정 일자, ORM이 save할 때'마다' 현재 날짜/시간으로 갱신
   ```

   

5. 수정 후 다시 `makemigration`하면 뜨는 두 가지 질문에 대해 각각 `1 + Enter`, `Enter`를 입력

   `$ python manage.py makemigrations`

   ```
   You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.   
   
    1) Provide a one-off default now (will be set on all existing rows)
    2) Quit, and let me add a default in models.py
   Select an option: 1
   ```

   

   ```
   Please enter the default value now, as valid Python
   You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
   The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
   Type 'exit' to exit this prompt
   [default: timezone.now] >>>
   ```

   

6. 새롭게 생성된 `articles/migrations/0002_auto_날짜.py`를 migrate하기

   `python manage.py migrate`



### ADMIN_계정생성 Article 등록



1. `http://127.0.0.1:8000/admin/`페이지에 접근 가능한 superuser를 admin이라는 이름으로 생성 (패스워드는 입력시에도 보이지 않음)

   `python manage.py createsuperuser`

   ```bash
   사용자 이름 (leave blank to use 'username'): admin
   이메일 주소: email@gmail.com
   Password: 
   Password (again):
   ```

   

   > 패스워드 입력 시 아래와 같은 메시지가 발생하면 `y`를 입력하거나, `N` 입력 후 비밀번호 재설정 

   ```
   비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
   비밀번호가 너무 일상적인 단어입니다.
   비밀번호가 전부 숫자로 되어 있습니다.
   Bypass password validation and create user anyway? [y/N]: y
   Superuser created successfully.
   ```

    

2. 서버를 `Ctrl + c`로 중단한 후 재실행하여, `http://127.0.0.1:8000/admin/` 페이지에 사용자 이름(admin)과 비밀번호 입력

3. `articles`디렉토리의 `admin.py`에 `articles/models.py`에서 작성한 `class Article` 내용 추가하고 새로고침하면, admin페이지에서도 확인 가능

   ```python
   # articles/admin.py
   
   from django.contrib import admin
   # models.py 에서 작성한 Article import
   from .models import Article
   
   # Register your models here.
   admin.site.register(Article)
   ```



### VIEW_Article 사용

1. 위에서 작성한 `model`을 사용해보기 위해, `views.py`의 `index` 내용을 수정

   ```python
   # articles/views.py
   
   from django.shortcuts import render
   # models.py에서 작성한 Article을 사용해야하므로 import
   from .models import Article
   
   # Create your views here.
   
   # 기존 내용
   # def index(request):
   #     return render(request, 'articles/index.html')
   
   def index(request):
       articles = Article.objects.all()
       context= {
           'articles': articles
       }
       return render(request, 'articles/index.html', context)
   ```



### TEMPLATE_articles 사용

1. `articles/templates/articles/` 경로의`index.html`도 `model index`에서 정의한 `articles`를 사용할 수 있도록 수정

   ```django
   <!-- articles/templates/articles/index.html -->
   
   {% extends 'base.html' %}
   {% comment %} base.html의 내용을 이어서 받아옴 {% endcomment %}
   
   {% block content %}
       <h1>INDEX</h1>
       <hr>
       {% for article in articles %}
           <p>제목: {{ article.title }}</p>
           <p>내용: {{ article.content }}</p>
           <hr>
       {% endfor %}
   {% endblock content %}
   ```

2. `Ctrl + c`로 서버 중단 후 재실행하면, 아직 사용자가 생성한 내용(title, content)이 없으므로 `INDEX`만 확인 가능



### URL_게시글 작성

1. `articles/urls.py`에 `new`와 `create` 라는 게시글 작성 관련 경로를 추가

   ```python
   # articles/urls.py
   # crud/urls.py와 연결됨
   
   from django.urls import path
   
   # articles 폴더(.) 안에 있는 view.py를 import
   from . import views
   
   # app 이름 설정 (나중에 'articles:index'처럼 앱 이름으로 사용 가능)
   app_name = 'articles'
   
   urlpatterns = [
       path('', views.index, name='index'),  # 기본주소 http://127.0.0.1:8000/articles
       
       # new와 create라는 경로 각각 추가
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
   ]
   ```



### VIEW_게시글 작성/GET METHOD

1. articles/views.py에 url에 추가된 new, create에 대한 정의를 추가

   ```python
   # articles/views.py
   
   from django.shortcuts import render
   # models.py에서 작성한 Article을 사용해야하므로 import
   from .models import Article
   
   # Create your views here.
   
   # 기존 내용
   # def index(request):
   #     return render(request, 'articles/index.html')
   
   def index(request):
       # 모든 게시글을 조회하는 페이지
       articles = Article.objects.all()
       context= {
           'articles': articles
       }
       return render(request, 'articles/index.html', context)
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       # new로 부터 title과 content를 받아서 저장
       title= request.GET.get('title')
       content= request.GET.get('content')
           
       article= Article(title=title, content=content)
       article.save()  # 저장 필요
   
       return render(request, 'articles/create.html')
   ```

   

### TEMPLATE_게시글 작성/GET METHOD

1. `articles/templates/articles/` 경로에 new.html, create.html 파일을 생성

   ```django
   <!-- articles/templates/articles/new.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>NEW</h1>
     {% comment %} action: url에서 articles앱의 create로 경로 이동
     (즉, views.py 내부에 정의된 create의 article.save()를 활용하기 위함) {% endcomment %}
     <form action="{% url 'articles:create' %}" method="GET">
       <label for="title">Title: </label>
       <input type="text" id="title" name="title">
       <label for="content">Content: </label>
       <textarea name="content" id="content" cols="30" rows="10"></textarea>
       <input type="submit" value="작성">
     </form>
     <hr>
   {% endblock %}
   ```

   ```django
   <!--articles/templates/articles/create.html-->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>CREATE</h1>
   {% endblock %}
   
   ```

   

2. `Ctrl + c`로 서버 중단 후 재실행한 뒤, `http://127.0.0.1:8000/articles/new/`에 `제목1`, `내용1`을 기입하면 url이 아래와 같이 변경됨 (보안 상 좋지 않으므로, 다음 절차에서 POST방식으로 csrf_token을 삽입 예정)

   ```
   http://127.0.0.1:8000/articles/create/?title=제목1&content=내용1
   ```

3. `http://127.0.0.1:8000/articles/` 페이지에 작성한 내용이 반영됨



### VIEW_POST METHOD

1. `views.py`에서 `create`의 `GET 방식`을 `POST 방식`으로 변경

   ```python
   # articles/views.py
   
   from django.shortcuts import render
   # models.py에서 작성한 Article을 사용해야하므로 import
   from .models import Article
   
   # Create your views here.
   
   # 기존 내용
   # def index(request):
   #     return render(request, 'articles/index.html')
   
   def index(request):
       articles = Article.objects.all()
       context= {
           'articles': articles
       }
       return render(request, 'articles/index.html', context)
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       # new로 부터 title과 content를 받아서 저장
       # title= request.GET.get('title')
       # content= request.GET.get('content')
   
       # GET 방식을 POST로 변경
       title= request.POST.get('title')
       content= request.POST.get('content')
   
       article= Article(title=title, content=content)
       article.save()  # 저장 필요
   
       return render(request, 'articles/create.html')
   ```

   

### TEMPLATE_POST METHOD

1. `articles/templates/articles/` 경로의 `new.html`에 `csrf_token`을 추가하고, `method를 POST`로 수정

   ```django
   <!-- articles/templates/articles/new.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>NEW</h1>
     {% comment %} action: url에서 articles앱의 create로 경로 이동
     (즉, views.py 내부에 정의된 create의 article.save()를 활용하기 위함) {% endcomment %}
     <form action="{% url 'articles:create' %}" method="POST">
       {% comment %} csrf_token으로 보안 유지 {% endcomment %}
       {% csrf_token %}
       <label for="title">Title: </label>
       <input type="text" id="title" name="title">
       <label for="content">Content: </label>
       <textarea name="content" id="content" cols="30" rows="10"></textarea>
       <input type="submit" value="작성">
     </form>
     <hr>
   {% endblock %}
   ```

2. `Ctrl + c`로 서버 중단 후 재실행한 뒤, `http://127.0.0.1:8000/articles/new/`에 `post제목`, `post내용`을 기입하더라도 입력한 내용이 url에 반영되지 않으며,  `http://127.0.0.1:8000/articles/`에서 확인 가능

   ```
   http://127.0.0.1:8000/articles/create/
   ```



### TEMPLATE_이전/다음 페이지 이동

1. 게시글 `작성(new.html)` 중 다시 `index페이지`로 돌아갈 수 있도록 `BACK` `a태그` 추가

   ```django
   <!-- articles/templates/articles/new.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>NEW</h1>
     {% comment %} action: url에서 articles앱의 create로 경로 이동
     (즉, views.py 내부에 정의된 create의 article.save()를 활용하기 위함) {% endcomment %}
     <form action="{% url 'articles:create' %}" method="POST">
       {% comment %} csrf_token으로 보안 유지 {% endcomment %}
       {% csrf_token %}
       <label for="title">Title: </label>
       <input type="text" id="title" name="title">
       <label for="content">Content: </label>
       <textarea name="content" id="content" cols="30" rows="10"></textarea>
       <input type="submit" value="작성">
     </form>
     <hr>
     {% comment %} 전체 목록을 보여주는 index 페이지로 되돌아 갈 수 있도록 {% endcomment %}
     <a href="{% url 'articles:index' %}">BACK</a>
   {% endblock %}
   ```

   

2. `초기화면(index.html)`에서 게시글 `작성(new)`페이지에 진입할 수 있도록 `NEW` `a태그` 추가

   ```django
   <!-- articles/templates/articles/index.html -->
   
   {% extends 'base.html' %}
   {% comment %} base.html의 내용을 이어서 받아옴 {% endcomment %}
   
   {% block content %}
       <h1>INDEX</h1>
       <br>
       {% comment %} 게시글 작성 페이지로 갈 수 있도록 {% endcomment %}
       <a href="{% url 'articles:new' %}">NEW</a>
   	<hr>
       {% for article in articles %}
           <p>제목: {{ article.title }}</p>
           <p>내용: {{ article.content }}</p>
           <hr>
       {% endfor %}
   {% endblock content %}
   ```

   

3. ★중요) `redirect`를 추가로 `import`하고, 게시글 작성(create) 후 index페이지로 재접근 할 수 있도록 return 수정

   ```python
   # articles/views.py
   
   from django.shortcuts import render, redirect   # 페이지 재진입을 위해 redirect 추가로 import
   # models.py에서 작성한 Article을 사용해야하므로 import
   from .models import Article
   
   # Create your views here.
   
   # 기존 내용
   # def index(request):
   #     return render(request, 'articles/index.html')
   
   def index(request):
       articles = Article.objects.all()
       context= {
           'articles': articles
       }
   
       return render(request, 'articles/index.html', context)
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       # new로 부터 title과 content를 받아서 저장
       # title= request.GET.get('title')
       # content= request.GET.get('content')
   
       # GET 방식을 POST로 변경
       title= request.POST.get('title')
       content= request.POST.get('content')
   
       article= Article(title=title, content=content)
       article.save()  # 저장 필요
   
       # return render(request, 'articles/create.html')
       return redirect('articles:index')
   ```

   



### TEMPLATE_게시글 순서

1. 게시글을 `역순`으로 나열할 수 있도록`index`의 `articles` 수정 (최근 게시물이 상단에 배치)

   ```python
   # articles/views.py
   
   from django.shortcuts import render, redirect   # 페이지 재진입을 위해 redirect 추가로 import
   # models.py에서 작성한 Article을 사용해야하므로 import
   from .models import Article
   
   # Create your views here.
   
   # 기존 내용
   # def index(request):
   #     return render(request, 'articles/index.html')
   
   def index(request):
       # articles = Article.objects.all()
       # articles = Article.objects.all()[::-1]    # 파이썬이 변경
       articles = Article.objects.order_by('-id')  # ORM으로 순서 변경
       context= {
           'articles': articles
       }
       
       return render(request, 'articles/index.html', context)
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       # new로 부터 title과 content를 받아서 저장
       # title= request.GET.get('title')
       # content= request.GET.get('content')
   
       # GET 방식을 POST로 변경
       title= request.POST.get('title')
       content= request.POST.get('content')
   
       article= Article(title=title, content=content)
       article.save()  # 저장 필요
   
       # return render(request, 'articles/create.html')
       return redirect('articles:index')
   ```



### MODEL_게시글 admin 내 표시

1. `http://127.0.0.1:8000/admin/articles/article/` 페이지에서 Article object(숫자)로 표기되는 것을 변경하기 위해, models.py에 내용 추가 (별도의 migration 생성 필요 X)

   ```python
   # articles/models.py
   
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       # id(PK, primary key) 자동 생성
       # makemigrations 후 생성되는 migrations/0001_initial.py 파일에서 확인 가능
       
       title = models.CharField(max_length=10) # 제목의 데이터 타입 CharField()는 글자 수 제한 필요(max_length가 필수 인자) 
       content = models.TextField()            # 글자 수 제한 없음
       
       # 새롭게 마이그레이션 생성하면, 0002에 추가될 내용
       created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add: 최초 생성일자에'만' 현재 날짜/시간으로 갱신
       updated_at = models.DateTimeField(auto_now=True)        # auto_now: 최종 수정 일자, ORM이 save할 때'마다' 현재 날짜/시간으로 갱신
   
       # DB에 영향을 미치는 것이 아니므로, migration을 새롭게 생성할 필요 없음
       def __str__(self):
           return f'{self.id}번 글 - {self.title} / {self.content}'
   ```

   

### ADMIN_생성/수정 일자 조회

1. `admin페이지`는 기본적으로 사용자가 입력한 값(title, content)에 대해서만 조회가 가능하므로, created_at과 updated_at또한 반영될 수 있도록 `admin.py` 수정

   ```python
   # articles/admin.py
   
   from django.contrib import admin
   # models.py 에서 작성한 Article import
   from .models import Article
   
   # Register your models here.
   # 기본적으로 사용자가 입력한 부분만 admin페이지에서 조회할 수 있기때문에,
   # 생성일자는 추가적으로 조회할 수 있도록 하단 수정
   class ArticleAdmin(admin.ModelAdmin):
       list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
   
   admin.site.register(Article, ArticleAdmin)
   ```

2. `http://127.0.0.1:8000/admin/articles/article/` 새로고침 조회

