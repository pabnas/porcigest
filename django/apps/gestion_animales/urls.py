from django.urls import path
from . import views

app_name = 'gestion_animales'
urlpatterns = [
    path('', views.index, name='index'),
    
    # gestacion
    path('gestacion/', views.gestacion_index, name='gestacion'),
    path('gestacion/resumen', views.gestacion_resumen, name='gestacion_resumen', kwargs={'navbar': 'gestacion_resumen'}),
    path('gestacion/registrar', views.gestacion_register, name='gestacion_registrar', kwargs={'navbar': 'gestacion_registrar'}),
    
    # inventario
    path('inventario/', views.inventario_index, name='inventario'),
    path('inventario/resumen', views.inventario_resumen, name='inventario_resumen', kwargs={'navbar': 'inventario_resumen'}),
    path('inventario/registrar', views.inventario_register, name='inventario_registrar', kwargs={'navbar': 'inventario_registrar'}),
    
    # lactancia
    path('lactancia/', views.lactancia_index, name='lactancia'),
    path('lactancia/resumen', views.lactancia_resumen, name='lactancia_resumen', kwargs={'navbar': 'lactancia_resumen'}),
    path('lactancia/registrar', views.lactancia_register, name='lactancia_registrar', kwargs={'navbar': 'lactancia_registrar'}),
    
    # movimientos
    path('movimientos/', views.movimientos_index, name='movimientos'),
    path('movimientos/resumen', views.movimientos_resumen, name='movimientos_resumen', kwargs={'navbar': 'movimientos_resumen'}),
    path('movimientos/registrar', views.movimientos_register, name='movimientos_registrar', kwargs={'navbar': 'movimientos_registrar'}),
    
    # precebos
    path('precebos/', views.precebos_index, name='precebos'),
    path('precebos/resumen', views.precebos_resumen, name='precebos_resumen', kwargs={'navbar': 'precebos_resumen'}),
    path('precebos/registrar', views.precebos_register, name='precebos_registrar', kwargs={'navbar': 'precebos_registrar'}),

    # ficha_cerdos
    path('ficha_cerdos/', views.ficha_cerdos_index, name='ficha_cerdos'),
    path('ficha_cerdos/resumen', views.ficha_cerdos_resumen, name='ficha_cerdos_resumen', kwargs={'navbar': 'ficha_cerdos_resumen'}),
    path('ficha_cerdos/registrar', views.ficha_cerdos_register, name='ficha_cerdos_registrar', kwargs={'navbar': 'ficha_cerdos_registrar'}),
]