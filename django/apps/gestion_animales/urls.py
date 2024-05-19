from django.urls import path
from . import views

app_name = 'gestion_animales'
urlpatterns = [
    path('', views.index, name='index'),

    # gestacion
    path('gestacion/', views.gestacion_index, name='gestacion'),
    path('gestacion/resumen', views.gestacion_resumen, name='gestacion_resumen', kwargs={'navbar': 'gestacion_resumen'}),
    path('gestacion/registrar', views.gestacion_register, name='gestacion_registrar', kwargs={'navbar': 'gestacion_registrar'}),
    path('gestacion/list_gestacion', views.list_gestacion, name='list_gestacion'),

    # inventario
    path('inventario/', views.inventario_index, name='inventario'),
    path('inventario/resumen', views.inventario_resumen, name='inventario_resumen', kwargs={'navbar': 'inventario_resumen'}),
    path('inventario/registrar', views.inventario_register, name='inventario_registrar', kwargs={'navbar': 'inventario_registrar'}),
    path('inventario/list_inventario', views.list_inventario, name='list_inventario'),

    # lactancia
    path('lactancia/', views.lactancia_index, name='lactancia'),
    path('lactancia/resumen', views.lactancia_resumen, name='lactancia_resumen', kwargs={'navbar': 'lactancia_resumen'}),
    path('lactancia/registrar', views.lactancia_register, name='lactancia_registrar', kwargs={'navbar': 'lactancia_registrar'}),
    path('lactancia/list_partos', views.list_partos, name='list_partos'),

    # movimientos
    path('movimientos/', views.movimientos_index, name='movimientos'),
    path('movimientos/resumen', views.movimientos_resumen, name='movimientos_resumen', kwargs={'navbar': 'movimientos_resumen'}),
    path('movimientos/registrar', views.movimientos_register, name='movimientos_registrar', kwargs={'navbar': 'movimientos_registrar'}),
    path('movimientos/list_movimientos', views.list_movimientos, name='list_movimientos'),

    # precebos
    path('precebos/', views.precebos_index, name='precebos'),
    path('precebos/resumen', views.precebos_resumen, name='precebos_resumen', kwargs={'navbar': 'precebos_resumen'}),
    path('precebos/registrar', views.precebos_register, name='precebos_registrar', kwargs={'navbar': 'precebos_registrar'}),
    path('precebos/list_lotes_lechones', views.list_lotes_lechones, name='list_lotes_lechones'),

    # ficha_cerdos
    path('ficha_cerdos/', views.ficha_cerdos_index, name='ficha_cerdos'),
    path('ficha_cerdos/resumen', views.ficha_cerdos_resumen, name='ficha_cerdos_resumen', kwargs={'navbar': 'ficha_cerdos_resumen'}),
]