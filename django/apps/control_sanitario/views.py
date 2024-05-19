from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from apps.control_sanitario.forms import MedicamentosForm, TratamientoLotesForm, TratamientosAnimalesForm

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
