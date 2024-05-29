from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from apps.utils import allowed_users
from models import Medicamentos
from models import Tratamientos
from models import TratamientosAnimales
from models import TratamientoLotes

from apps.control_sanitario.forms import MedicamentosForm, MedicamentosSalidaForm, TratamientoLotesForm, TratamientosAnimalesForm, TratamientosForm

# index
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def index(request):
    return redirect('control_sanitario:inventario_resumen')

# inventario
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def inventario_index(request):
    return redirect('control_sanitario:inventario_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def list_medicamentos(_request):
    medicamentos = list(Medicamentos.objects.values())
    data = {'medicamentos': medicamentos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def inventario_resumen(request, **kwargs):
    return render(request, 'control_sanitario/inventario/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def inventario_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=MedicamentosForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('control_sanitario:inventario_registrar')
    else:
        form=MedicamentosForm()
    mydict['form']=form
    return render(request, 'control_sanitario/inventario/register.html', mydict)


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def inventario_salida(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=MedicamentosSalidaForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('control_sanitario:vacunacion_registrar_tratamiento_animal')
    else:
        form=MedicamentosSalidaForm()
    mydict['form']=form
    return render(request, 'control_sanitario/inventario/salida.html', mydict)


# tratamientos
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def tratamientos_index(request):
    return redirect('control_sanitario:tratamientos_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def list_tratamientos(_request):
    tratamientos = list(Tratamientos.objects.values())
    data = {'tratamientos': tratamientos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def tratamientos_resumen(request, **kwargs):
    return render(request, 'control_sanitario/tratamientos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def tratamientos_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=TratamientosForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('control_sanitario:vacunacion_registrar_tratamiento_animal')
    else:
        form=TratamientosForm()
    mydict['form']=form
    return render(request, 'control_sanitario/tratamientos/register.html', mydict)


# vacunacion
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def vacunacion_index(request):
    return redirect('control_sanitario:vacunacion_resumen')

# @login_required(login_url='/login', redirect_field_name=None)
# @allowed_users(allowed_roles=['administrador'])
# def list_movimientos(_request):
#     movimientos = list(
#         Movimientos.objects.values(
#             'id_movimiento',
#             'id_animal__numero_identificacion_animal',
#             'fecha',
#             'area_origen__nombre_area',
#             'area_destino__nombre_area',
#         )
#     )
#     data = {'movimientos': movimientos}
#     return JsonResponse(data)
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def list_vacunacion(_request):
    vacunacion = list(
        TratamientosAnimales.objects.values(
            'id_tratamiento_animal',
            'id_animal__numero_identificacion_animal',
            'fecha_tratamiento_animal',
            'observaciones_animal',
            'id_tratamiento__tipo_tratamiento'
        )
    )
    data = {'vacunacion': vacunacion}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def list_lotes(_request):
    lotes = list(
        TratamientoLotes.objects.values(
            'id_lote_tratamiento',
            'id_lote',
            'fecha_aplicacion_lote',
            'dosis_lote',
            'observaciones_lote',
            'id_tratamiento__tipo_tratamiento'
        )
    )
    data = {'lotes': lotes}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def vacunacion_resumen(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/resumen.html')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def lotes_resumen(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/resumen_lotes.html')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def vacunacion_register_tratamiento_animal(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=TratamientosAnimalesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('control_sanitario:vacunacion_registrar_tratamiento_animal')
    else:
        form=TratamientosAnimalesForm()
    mydict['form']=form
    return render(request, 'control_sanitario/vacunacion/register_tratamiento_animal.html', mydict)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador', 'veterinario'])
def vacunacion_register_tratamiento_lotes(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=TratamientoLotesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('control_sanitario:vacunacion_registrar_tratamiento_lotes')
    else:
        form=TratamientoLotesForm()
    mydict['form']=form
    return render(request, 'control_sanitario/vacunacion/register_tratamiento_lotes.html', mydict)
