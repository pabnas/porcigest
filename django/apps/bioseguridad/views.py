from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse


from apps.utils import allowed_users
from models import IngresoVehiculos
from apps.bioseguridad.forms import IngresoVehiculosForm

# index
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def index(request):
    return redirect('bioseguridad:ingreso_vehiculos_resumen')

@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def list_vehiculos(_request):
    vehiculos = list(IngresoVehiculos.objects.values())
    data = {'vehiculos': vehiculos}
    return JsonResponse(data)

# personas
@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def ingreso_vehiculos_index(request):
    return redirect('bioseguridad:ingreso_vehiculos_resumen')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def ingreso_vehiculos_resumen(request, **kwargs):
    return render(request, 'bioseguridad/ingreso_vehiculos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
@allowed_users(allowed_roles=['administrador'])
def ingreso_vehiculos_register(request, **kwargs):
    mydict={}
    if request.method == 'POST':
        form=IngresoVehiculosForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('bioseguridad:ingreso_vehiculos_registrar')
    else:
        form=IngresoVehiculosForm()
    mydict['form']=form
    return render(request, 'bioseguridad/ingreso_vehiculos/register.html', mydict)

