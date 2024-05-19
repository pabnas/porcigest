from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from apps.bioseguridad.forms import IngresoVehiculosForm

# index
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    return redirect('bioseguridad:ingreso_vehiculos_resumen')

# personas
@login_required(login_url='/login', redirect_field_name=None)
def ingreso_vehiculos_index(request):
    return redirect('bioseguridad:ingreso_vehiculos_resumen')


@login_required(login_url='/login', redirect_field_name=None)
def ingreso_vehiculos_resumen(request, **kwargs):
    return render(request, 'bioseguridad/ingreso_vehiculos/resumen.html')


@login_required(login_url='/login', redirect_field_name=None)
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

