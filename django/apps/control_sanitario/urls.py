from django.urls import path
from . import views

app_name = 'control_sanitario'
urlpatterns = [
    path('', views.index, name='index'),

    # inventario
    path('inventario/', views.inventario_index, name='inventario'),
    path('inventario/resumen', views.inventario_resumen, name='inventario_resumen', kwargs={'navbar': 'inventario_resumen'}),
    path('inventario/registrar', views.inventario_register, name='inventario_registrar', kwargs={'navbar': 'inventario_registrar'}),
    path('inventario/salida', views.inventario_salida, name='inventario_salida', kwargs={'navbar': 'inventario_salida'}),

    # tratamientos
    path('tratamientos/', views.tratamientos_index, name='tratamientos'),
    path('tratamientos/resumen', views.tratamientos_resumen, name='tratamientos_resumen', kwargs={'navbar': 'tratamientos_resumen'}),
    path('tratamientos/registrar', views.tratamientos_register, name='tratamientos_registrar', kwargs={'navbar': 'tratamientos_registrar'}),

    # vacunaciones
    path('vacunacion/', views.vacunacion_index, name='vacunacion'),
    path('vacunacion/resumen', views.vacunacion_resumen, name='vacunacion_resumen', kwargs={'navbar': 'vacunacion_resumen'}),
    path('vacunacion/registrar', views.vacunacion_register, name='vacunacion_registrar', kwargs={'navbar': 'vacunacion_registrar'}),
]