from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from models import IngresoVehiculos

# index
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('bioseguridad:ingreso_personas_resumen')

@login_required(login_url='/login', redirect_field_name=None)
def list_vehiculos(_request):
    vehiculos = list(IngresoVehiculos.objects.values())
    data = {'vehiculos': vehiculos}
    return JsonResponse(data)

# personas
@login_required(login_url='/login', redirect_field_name=None)
def ingreso_personas_index(request):
    return redirect('bioseguridad:ingreso_personas_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def ingreso_personas_resumen(request, **kwargs):
    return render(request, 'bioseguridad/ingreso_personas/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def ingreso_personas_register(request, **kwargs):
    return render(request, 'bioseguridad/ingreso_personas/register.html')

