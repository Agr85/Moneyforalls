from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('list_cursos/', views.list_cursos, name='list_cursos'),
    path('obtener_paises/', views.obtener_paises, name='obtener_paises'),
    path('accounts/login/', views.registro, name='registro'),
    path('services/', views.services, name='services')
]