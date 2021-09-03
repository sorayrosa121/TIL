"""pjt04 URL Configuration

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
# pjt04/urls.py

from django.contrib import admin
from django.urls import path, include   # include import

# http://127.0.0.1:8000/ 뒷부분에 추가로 붙게되는 url
urlpatterns = [
    path('movies/', include('movies.urls')),    ### http://127.0.0.1:8000/movies/
                                                # movies/urls.py에 정의된 path들도 포함
    path('admin/', admin.site.urls),            ### http://127.0.0.1:8000/admin/
                                                # django에서 생성
]
