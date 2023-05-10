from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('list_cursos/', views.list_cursos, name='list_cursos')
]