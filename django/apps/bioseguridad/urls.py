from django.urls import path
from . import views

app_name = 'bioseguridad'
urlpatterns = [
    path('', views.index, name='index'),
    # ingreso personas
    path('ingreso_vehiculos/', views.ingreso_vehiculos_index, name='ingreso_vehiculos'),
    path('ingreso_vehiculos/resumen', views.ingreso_vehiculos_resumen, name='ingreso_vehiculos_resumen', kwargs={'navbar': 'ingreso_vehiculos_resumen'}),
    path('ingreso_vehiculos/registrar', views.ingreso_vehiculos_register, name='ingreso_vehiculos_registrar', kwargs={'navbar': 'ingreso_vehiculos_registrar'}),
    path('ingreso_vehiculos/list_vehiculos', views.list_vehiculos, name='list_vehiculos'),
]