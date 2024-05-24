import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseBadRequest

from apps.utils import allowed_users
from models import InventarioAnimales
from models import RegistroInseminaciones
from models import RegistroPartos
from models import Movimientos
from models import LotesLechones

from apps.gestion_animales.forms import InventarioAnimalesForm
from apps.gestion_animales.forms import LotesLechonesForm, MovimientosForm
from apps.gestion_animales.forms import OrigenExternoForm, OrigenInternoForm, VentaUnidadForm
from apps.gestion_animales.forms import VentaUnidadForm
from apps.gestion_animales.forms import RegistroInseminacionesForm
from apps.gestion_animales.forms import RegistroPartosForm, VentaLotesForm

# index
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def index(request):
    return redirect('gestion_animales:gestacion_resumen')

# gestacion
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def gestacion_index(request):
    return redirect('gestion_animales:gestacion_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_gestacion(_request):
    gestacion_all_rows = RegistroInseminaciones.objects.values()
    for row in gestacion_all_rows:
        row['fecha_parto_estimada'] = row['fecha_inseminacion'] + datetime.timedelta(days=114)
    gestacion = list(gestacion_all_rows)
    data = {'gestacion': gestacion}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def gestacion_resumen(request, **kwargs):
    return render(request, 'gestion_animales/gestacion/resumen.html')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def gestacion_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=RegistroInseminacionesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:gestacion_registrar')
    else:
        form=RegistroInseminacionesForm()
    mydict['form']=form
    return render(request, 'gestion_animales/gestacion/register.html', mydict)

# inventario
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def inventario_index(request):
    return redirect('gestion_animales:inventario_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_inventario(_request):
    inventario = list(InventarioAnimales.objects.values())
    data = {'inventario': inventario}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def inventario_resumen(request, **kwargs):
    return render(request, 'gestion_animales/inventario/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def inventario_register_ingreso(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        dict = request.POST
        
        # extract origen_interno keys
        origen_interno_dict = {}
        for key, value in dict.items():
            if key.startswith("origen_interno-"):
                new_key = key.replace("origen_interno-", "")
                origen_interno_dict[new_key] = value
        
        # extract origen_externo keys
        origen_externo_dict = {}
        for key, value in dict.items():
            if key.startswith("origen_externo-"):
                new_key = key.replace("origen_externo-", "")
                origen_externo_dict[new_key] = value

        # logger.warning(f'dict: {dict}')
        # logger.warning(f'origen_externo_dict: {origen_externo_dict}')
        # logger.warning(f'origen_interno_dict: {origen_interno_dict}')
        
        form=InventarioAnimalesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            animal = form.customSave()
            
            if form.cleaned_data['origen'] == 'I':
                form_origen_interno = OrigenInternoForm(origen_interno_dict)
                if form_origen_interno.is_valid():
                    form_origen_interno.save()
                else:
                    return HttpResponseBadRequest("Invalid internal origin form data")
            elif form.cleaned_data['origen'] == 'E':
                form_origen_externo = OrigenExternoForm(origen_externo_dict)
                form_origen_externo.instance.id_animal = animal
                form_origen_externo.instance.peso_compra = animal.peso
                form_origen_externo.instance.etapa_productiva_ingreso = animal.estado_productivo
                if form_origen_externo.is_valid():
                    form_origen_externo.save()
                else:
                    return HttpResponseBadRequest("Invalid external origin form data")
            else:
                return HttpResponseBadRequest("Invalid origin data")

            return redirect('gestion_animales:inventario_registrar_ingreso')
    else:
        form=InventarioAnimalesForm()
    mydict['form']=form
    return render(request, 'gestion_animales/inventario/register_ingreso.html', mydict)


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def inventario_register_salida(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=VentaUnidadForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:inventario_registrar_salida')
    else:
        form=VentaUnidadForm()
    mydict['form']=form
    return render(request, 'gestion_animales/inventario/register_salida.html', mydict)

# lactancia
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def lactancia_index(request):
    return redirect('gestion_animales:lactancia_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_partos(_request):
    partos = list(RegistroPartos.objects.values())
    data = {'partos': partos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def lactancia_resumen(request, **kwargs):
    return render(request, 'gestion_animales/lactancia/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def lactancia_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=RegistroPartosForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:lactancia_registrar')
    else:
        form=RegistroPartosForm()
    mydict['form']=form
    return render(request, 'gestion_animales/lactancia/register.html', mydict)

# movimientos
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def movimientos_index(request):
    return redirect('gestion_animales:movimientos_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_movimientos(_request):
    movimientos = list(Movimientos.objects.values())
    data = {'movimientos': movimientos}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def movimientos_resumen(request, **kwargs):
    return render(request, 'gestion_animales/movimientos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def movimientos_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=MovimientosForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:movimientos_registrar')
    else:
        form=MovimientosForm()
    mydict['form']=form
    return render(request, 'gestion_animales/movimientos/register.html', mydict)

# precebos
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def precebos_index(request):
    return redirect('gestion_animales:precebos_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_lotes_lechones(_request):
    lotes_lechones = list(LotesLechones.objects.values())
    data = {'lotes_lechones': lotes_lechones}
    return JsonResponse(data)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def precebos_resumen(request, **kwargs):
    return render(request, 'gestion_animales/precebos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def precebos_register_ingreso(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=LotesLechonesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:precebos_registrar_ingreso')
    else:
        form=LotesLechonesForm()
    mydict['form']=form
    return render(request, 'gestion_animales/precebos/register_ingreso.html', mydict)

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def precebos_register_salida(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=VentaLotesForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('gestion_animales:precebos_registrar_salida')
    else:
        form=VentaLotesForm()
    mydict['form']=form
    return render(request, 'gestion_animales/precebos/register_salida.html', mydict)
