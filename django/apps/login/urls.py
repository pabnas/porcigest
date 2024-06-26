from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactanos', views.contactanos_page, name='contactenos'),
    path('login', views.login_form, name='login'),
    path('login_form', views.login_request, name='login_request'),
    path('logout', views.logout_request, name='logout'),
]