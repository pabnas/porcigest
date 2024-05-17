from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# index
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('control_sanitario:inventario_resumen')

# inventario
@login_required(login_url='/login', redirect_field_name=None)
def inventario_index(request):
    return redirect('control_sanitario:inventario_resumen')


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
def vacunacion_resumen(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
def vacunacion_register(request, **kwargs):
    return render(request, 'control_sanitario/vacunacion/register.html')
