from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from models import Medicamentos
from models import Tratamientos
from models import TratamientosAnimales

# index
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('control_sanitario:inventario_resumen')

# inventario
@login_required(login_url='/login', redirect_field_name=None)
def inventario_index(request):
    return redirect('control_sanitario:inventario_resumen')

@login_required(login_url='/login', redirect_field_name=None)
def list_medicamentos(_request):
    medicamentos = list(Medicamentos.objects.values())
    data = {'medicamentos': medicamentos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
def inventario_resumen(request, **kwargs):
    return render(request, 'control_sanitario/inventario/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def inventario_register(request, **kwargs):
    return render(request, 'control_sanitario/inventario/register.html')


@login_required(login_url='/login', redirect_field_name=None)
def inventario_salida(request, **kwargs):
    return render(request, 'control_sanitario/inventario/salida.html')


# tratamientos
@login_required(login_url='/login', redirect_field_name=None)
def tratamientos_index(request):
    return redirect('control_sanitario:tratamientos_resumen')

@login_required(login_url='/login', redirect_field_name=None)
def list_tratamientos(_request):
    tratamientos = list(Tratamientos.objects.values())
    data = {'tratamientos': tratamientos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
def tratamientos_resumen(request, **kwargs):
    return render(request, 'control_sanitario/tratamientos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def tratamientos_register(request, **kwargs):
    return render(request, 'control_sanitario/tratamientos/register.html')


# vacunacion
@login_required(login_url='/login', redirect_field_name=None)
def vacunacion_index(request):
    return redirect('control_sanitario:vacunacion_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def list_vacunacion(_request):
    vacunacion = list(
        TratamientosAnimales.objects.filter(id_tratamiento__tipo_tratamiento='Vacunación').values(
            'id_tratamiento_animal',
            'id_animal',
            'fecha_tratamiento_animal',
            'observaciones_animal',
            'id_tratamiento__tipo_tratamiento'
        )
    )
    data = {'vacunacion': vacunacion}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
def vacunacion_resumen(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def vacunacion_register(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/register.html')
