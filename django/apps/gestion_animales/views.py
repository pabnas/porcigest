from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# index
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('gestion_animales:gestacion_resumen')

# gestacion
@login_required(login_url='/login', redirect_field_name=None)
def gestacion_index(request):
    return redirect('gestion_animales:gestacion_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def gestacion_resumen(request, **kwargs):
    return render(request, 'gestion_animales/gestacion/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def gestacion_register(request, **kwargs):
    return render(request, 'gestion_animales/gestacion/register.html')

# inventario

@login_required(login_url='/login', redirect_field_name=None)
def inventario_index(request):
    return redirect('gestion_animales:inventario_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def inventario_resumen(request, **kwargs):
    return render(request, 'gestion_animales/inventario/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def inventario_register(request, **kwargs):
    return render(request, 'gestion_animales/inventario/register.html')

# lactancia

@login_required(login_url='/login', redirect_field_name=None)
def lactancia_index(request):
    return redirect('gestion_animales:lactancia_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def lactancia_resumen(request, **kwargs):
    return render(request, 'gestion_animales/lactancia/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def lactancia_register(request, **kwargs):
    return render(request, 'gestion_animales/lactancia/register.html')

# movimientos

@login_required(login_url='/login', redirect_field_name=None)
def movimientos_index(request):
    return redirect('gestion_animales:movimientos_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def movimientos_resumen(request, **kwargs):
    return render(request, 'gestion_animales/movimientos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def movimientos_register(request, **kwargs):
    return render(request, 'gestion_animales/movimientos/register.html')

# precebos

@login_required(login_url='/login', redirect_field_name=None)
def precebos_index(request):
    return redirect('gestion_animales:precebos_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def precebos_resumen(request, **kwargs):
    return render(request, 'gestion_animales/precebos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def precebos_register(request, **kwargs):
    return render(request, 'gestion_animales/precebos/register.html')

# ficha_cerdos

@login_required(login_url='/login', redirect_field_name=None)
def ficha_cerdos_index(request):
    return redirect('gestion_animales:ficha_cerdos_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def ficha_cerdos_resumen(request, **kwargs):
    return render(request, 'gestion_animales/ficha_cerdos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def ficha_cerdos_register(request, **kwargs):
    return render(request, 'gestion_animales/ficha_cerdos/register.html')
