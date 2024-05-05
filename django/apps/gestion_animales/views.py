from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('gestacion_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def resumen(request, **kwargs):
    return render(request, 'gestion_animales/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def register(request, **kwargs):
    return render(request, 'gestion_animales/register.html')
