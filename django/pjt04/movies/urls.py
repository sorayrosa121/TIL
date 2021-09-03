# movies/urls.py

from django.urls import path
from . import views     # ./views (즉, movies/views.py)에서 정의한(할) 내용 import

app_name ='movies'

urlpatterns = [
    path('', views.index, name='index'),            # http://127.0.0.1:8000/movies/
    path('new/', views.new, name='new'),            # http://127.0.0.1:8000/movies/new/
    path('create/', views.create, name='create'),

    # detail, edit, update, delete는 특정한 pk(id)를 url에 추가
    path('<int:pk>/', views.detail, name='detail'),     # http://127.0.0.1:8000/movies/1/
    path('<int:pk>/edit/', views.edit, name='edit'),    # http://127.0.0.1:8000/movies/1/edit
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
