from django.urls import path
from . import views

app_name = 'bioseguridad'
urlpatterns = [
    path('', views.index, name='index'),
    # ingreso personas
    path('ingreso_personas/', views.ingreso_personas_index, name='ingreso_personas'),
    path('ingreso_personas/resumen', views.ingreso_personas_resumen, name='ingreso_personas_resumen', kwargs={'navbar': 'ingreso_personas_resumen'}),
    path('ingreso_personas/registrar', views.ingreso_personas_register, name='ingreso_personas_registrar', kwargs={'navbar': 'ingreso_personas_registrar'}),
]