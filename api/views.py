from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Cursos, Registro
from .forms import RegistroForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
     if not request.session.get('email'):
        # El usuario no existe la session, redirigir a la página de registro
        return redirect('accounts/login/') 
     else:
        # El existe la session, redirigir a la página de index
        return redirect('index')      


def list_cursos(_request):
    cursos = list(Cursos.objects.values())
    data = {'cursos': cursos}
    return JsonResponse(data)




def obtener_paises(request):
    # Lógica para obtener los datos de los países
    paises = ['CU', 'AR', 'CA']  # Ejemplo de datos de los países

    return JsonResponse(paises, safe=False)


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Verificar si el correo ya existe en el modelo Registro
                registro = Registro.objects.get(email=email)
                # El correo ya existe, realizar el login y redirigir a la página principal
                # Puedes realizar el login manualmente o usar la funcionalidad de autenticación de Django
                # Aquí se muestra un ejemplo de login manual
                request.session['email'] = registro.email
                return redirect('index')
            except Registro.DoesNotExist:
                # El correo no existe, guardar los datos en el modelo Registro y redirigir a la página principal
                form.save()
                return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})