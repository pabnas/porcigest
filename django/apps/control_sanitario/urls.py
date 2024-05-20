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
    path('inventario/list_medicamentos', views.list_medicamentos, name='list_medicamentos'),


    # tratamientos
    path('tratamientos/', views.tratamientos_index, name='tratamientos'),
    path('tratamientos/resumen', views.tratamientos_resumen, name='tratamientos_resumen', kwargs={'navbar': 'tratamientos_resumen'}),
    path('tratamientos/registrar', views.tratamientos_register, name='tratamientos_registrar', kwargs={'navbar': 'tratamientos_registrar'}),
    path('tratamientos/list_tratamientos', views.list_tratamientos, name='list_tratamientos'),

    # vacunaciones
    path('vacunacion/', views.vacunacion_index, name='vacunacion'),
    path('vacunacion/resumen', views.vacunacion_resumen, name='vacunacion_resumen', kwargs={'navbar': 'vacunacion_resumen'}),
    path('vacunacion/registrar_tratamiento_animal', views.vacunacion_register_tratamiento_animal, name='vacunacion_registrar_tratamiento_animal', kwargs={'navbar': 'vacunacion_registrar_tratamiento_animal'}),
    path('vacunacion/registrar_tratamiento_lotes', views.vacunacion_register_tratamiento_lotes, name='vacunacion_registrar_tratamiento_lotes', kwargs={'navbar': 'vacunacion_registrar_tratamiento_lotes'}),
]