from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'base.html')

def contactanos_page(request):
    return render(request, 'contactanos.html')

def login_form(request):
    return render(request, 'login.html')


def login_request(request):
    data = dict()
    data['msg'] = "success"
    
    try:
        usuario = request.POST['usuario']
        password = request.POST['password']
        if password == '':
            raise Exception("Contraseña vacia")
        elif usuario == '':
            raise Exception("Usuario vacio")
        
        user = authenticate(username=usuario, password=password)
        if user is None:
            raise Exception("Usuario no existe o contraseña incorrecta")
        if user.is_active == False:
            raise Exception("Usuario inactivo")
        login(request, user)
        data['url'] = '/dashboard'
        return JsonResponse(data)
    except Exception as e:
        data['msg'] = str(e)
    return JsonResponse(data)

