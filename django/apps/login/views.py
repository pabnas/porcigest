from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from porcigest.sendgrid import send_mail_contact_us

# Create your views here.
def index(request):
    return render(request, 'base.html')

def contactanos_page(request):
    if request.method == 'POST':
        if 'nombre completo' in request.POST and 'correo' in request.POST and 'direccion' in request.POST and 'telefono' in request.POST and 'mensaje' in request.POST:
            nombre_completo = request.POST['nombre completo']
            correo = request.POST['correo']
            direccion = request.POST['direccion']
            telefono = request.POST['telefono']
            mensaje = request.POST['mensaje']
            send_mail_contact_us(
                nombre_completo=nombre_completo,
                correo=correo,
                direccion=direccion,
                telefono=telefono,
                mensaje=mensaje
            )
            return render(request, 'contactanos.html', {'msg': 'Pronto el administrador se pondrá en contacto con usted'})
        else:
            return render(request, 'contactanos.html', {'msg': 'Llene todos los campos del formulario'})
    return render(request, 'contactanos.html', {'msg': ''})

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

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
