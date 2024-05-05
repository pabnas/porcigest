from django.urls import path
from . import views

urlpatterns = [
    path('gestacion/', views.index, name='gestacion'),
    path('gestacion/resumen', views.resumen, name='gestacion_resumen', kwargs={'navbar': 'gestacion_resumen'}),
    path('gestacion/registrar', views.register, name='gestacion_registrar', kwargs={'navbar': 'gestacion_registrar'}),
]