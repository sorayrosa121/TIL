1. 새로운 프로젝트 Django_project를 만들고 vscode로 열기

2. vscode에서 Ctrl + Shift + P로 검색창 활성화 후 Open Settings(JSON)에 하단 내용 추가

   ```javascript
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

   

3. bash(Ctrl+`)에서 python 버전 확인

   `python --version`

4. 가상환경의 이름으로 venv로 생성

   `python -m venv venv`

5. git ignore 내용 검색

   `https://www.toptal.com/developers/gitignore`에서 python, Django, visual studio code, venv 키워드 입력

6. Django_project 프로젝트에 `.gitignore`파일 생성 후, `5. `번에서 생성한 내용 복사 붙여넣기

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

