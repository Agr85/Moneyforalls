from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Cursos

# Create your views here.

def index(request):
    return render(request, 'index.html')

def list_cursos(_request):
    cursos = list(Cursos.objects.values())
    data = {'cursos': cursos}
    return JsonResponse(data)  