1. 새로운 프로젝트 Django_project를 만들고 vscode로 열기

2. vscode에서 `Ctrl + Shift + P`로 검색창 활성화 후 Open Settings(JSON)에 하단 내용 추가

    ```json
   // settings.json
   
   {
     ... 생략 ...,
   
     // Django
     "files.associations": {
       "**/*.html": "html",
       "**/templates/**/*.html": "django-html",
       "**/templates/**/*": "django-txt",
       "**/requirements{/**,*}.{txt,in}": "pip-requirements"
     },
     "emmet.includeLanguages": {
       "django-html": "html"
     }
   }
   ```

   

3. bash(Ctrl + `)에서 python 버전 확인

     `python --version`

4. 가상환경의 이름으로 venv로 생성

     `python -m venv venv`

5. git ignore 내용 검색

    `https://www.toptal.com/developers/gitignore`에서 python, Django, visual studio code, venv 키워드 입력

6. Django_project 프로젝트에 `.gitignore`파일 생성 후, `5. `번에서 생성한 내용 붙여넣기

7. activate 시키기

     `source venv/Scripts/activate`

8.  pip list 확인하기

     `pip list`

9.  (deactivate 방법)

     `deactivate`

10. `7.`번으로 돌아가서 다시 venv 켜고, 장고 설치

     `source venv/Scripts/activate`

     `pip install django`

11. django_intro라는 이름으로 django 파일 생성

     `django-admin startproject django_intro .`

12. 서버 실행

     `python manage.py runserver`

13. bash에 뜨는 `http://127.0.0.1:8000/` 클릭, 혹은 주소 입력

14. Ctrl + C로 서버를 멈춘 후, articles라는 이름의 app 생성

     `python manage.py startapp articles`

15. ★중요) django_intro 폴더의 `settings.py` -> `INSTALLED_APPS`에 articles app추가

     ```python
     INSTALLED_APPS = [
         # django에서는 APPS을 사용할 때, 위에서부터 아래로 사용함
         'articles',
         
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
     ]
     ```

     

16. `settings.py`에서 `LANGUAGE_CODE`를 `ko-kr`로 변경 후 저장, `12.` 번으로 서버를 다시 실행하면 한국어로 설정 가능

     `LANGUAGE_CODE = 'ko-kr'`

     `TIME_ZONE = 'Asia/Seoul'`

17. `articles 디렉토리`에 `templates` 폴더 생성 -> `index.html` 파일 생성 및 내용 추가

     ```django
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
     </head>
     <body>
         <h1>articles 앱의 index.html</h1>
         <h2>만나서 반갑습니다. hello django</h2>
     </body>
     </html>
     ```

     

18. `django_intro`의 `urls.py`에 index 관련 내용 추가

     ```python
     from django.contrib import admin
     from django.urls import path
     
     #articles 폴더 안에 있는 view.py
     from articles import views
     
     urlpatterns = [
         # index라는 주소(http://127.0.0.1:8000/index)로 접속하면, views.index 함수를 실행
         path('index/', views.index),
         
         path('admin/', admin.site.urls),
     ]
     ```

     

19. `articles`의 `views.py` 내용 추가

     ```python
     from django.shortcuts import render
     
     # Create your views here.
     def index(request):
         return render(request, 'index.html')    # 'index.html'이라는 상대주소로도 참고 가능
     ```

     

20.  수정 내용이 모두 저장되었는지 확인 후, `12.` 서버 실행

     `python manage.py runserver`

21. `http://127.0.0.1:8000/index` 주소 입력

22. `Django_project`에 `templates`라는 디렉토리 생성 후, `base.html` 파일 생성

      ```django
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Document</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
      </head>
      <body>
          <nav class="navbar navbar-dark bg-dark">
              <div class="container-fluid">
                  <a class="navbar-brand" href="#">Navbar</a>
              </div>
          </nav>
      
          <h1>Template Inheritance(템플릿 상속)</h1>
      
          {% comment %} block content를 통해 {% endcomment %}
          {% block content %}
          {% endblock content %}
          
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
      </body>
      </html>
      ```

      

23. `django_intro`의 `settings.py`에 dir 관련 내용 추가

      ```python
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              
              # 경로 추가해주기
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

      

24. Django_project/templates 디렉토리에 dinner.html 파일 생성

      ```django
      {% comment %} base.html의 내용을 extends 해옴 {% endcomment %}
      {% extends 'base.html' %}
      
      {% block content %}
          <h1>안녕하세요! 저는 {{ info.name }} 입니다. </h1>
          <p>제가 좋아하는 과일은 {{ foods }} 입니다. </p>
          <p>{{ foods.0 }}를 제일 좋아합니다. </p>
      {% endblock content %}
      ```

      

25. urls.py에 throw 추가하기

      ```python
      from django.contrib import admin
      from django.urls import path
      from articles import views
      
      urlpatterns = [
          path('throw/', views.throw),
      
          path('admin/', admin.site.urls),
      ]
      ```

      

26. views.py

      ```
      def throw(request):
      
          return render(request, 'throw.html')
      ```

      

27. templates/throw.html 만들기

      ```
      ```

      

28. catch

29. catch.html 만들기

30. hello 추가

31. views.py 에서 hello

      ```
      # url에 있는 데이터를 받아오는 방법
      def hello(request, name):
          context = {
              'name': name
          }
          return render(request, 'hello.html', context)
      ```

      

32. hello.html



python manage.py startapp pages

settings.py에 pages 추가

articles/templates/articles

pages/templates/pages/index.html
