from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


from models import InventarioAnimales, MonitoreoAgua, RegistroPartos, LotesLechones

# Create your views here.
@login_required(login_url='/login', redirect_field_name=None)
def index(request):
    count_cerdos = InventarioAnimales.objects.all().count()
    count_lactancias = RegistroPartos.objects.all().count()
    count_lotes = LotesLechones.objects.all().count()
    
    try:
        last_nivel_agua = MonitoreoAgua.objects.latest('fecha_hora').nivel_agua_porcentaje
    except ObjectDoesNotExist:
        last_nivel_agua = 0
    
    # Get agua
    twenty_four_hours_ago = timezone.now() - timedelta(hours=24)
    data_last_24_hours = MonitoreoAgua.objects.filter(fecha_hora__gte=twenty_four_hours_ago)
    
    datetimes = [entry.fecha_hora.strftime('%Y-%m-%dT%H:%M:%S') for entry in data_last_24_hours]
    flujo_agua_litros_hora_values = [float(entry.flujo_agua_litros_hora) for entry in data_last_24_hours]
    chart_flujo_agua_data = {
        'labels': datetimes,
        'data': flujo_agua_litros_hora_values
    }
    
    # Get nacimientos data
    one_month_ago = timezone.now() - timedelta(days=30)
    data_last_month = RegistroPartos.objects.filter(fecha_parto__gte=one_month_ago)
    fecha_parto_values = [entry.fecha_parto.strftime('%Y-%m-%d') for entry in data_last_month]
    nacidos_vivos_values = [entry.nacidos_vivos for entry in data_last_month]

    # Combine fecha_parto and nacidos_vivos values into a dictionary
    chart_nacimientos_data = {
        'labels': fecha_parto_values,
        'data': nacidos_vivos_values
    }
    
    mydict = {
        'count_cerdos': count_cerdos,
        'count_lactancias': count_lactancias,
        'count_lotes': count_lotes,
        'last_nivel_agua': float(last_nivel_agua),
        'chart_flujo_agua_data': chart_flujo_agua_data,
        'chart_nacimientos_data': chart_nacimientos_data
    }
    logger.warning(f'dict = {mydict}')
    
    return render(request, 'dashboard.html', mydict)
