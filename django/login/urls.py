from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactanos', views.contactanos_page, name='contactanos')
]