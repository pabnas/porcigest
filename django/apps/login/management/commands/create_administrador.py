import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from models import *

GROUPS = ['administrador']
MODELS = [
    ("Areas", Areas),
    ("Corrales", Corrales),
    ("IngresoVehiculos", IngresoVehiculos),
    ("InventarioAnimales", InventarioAnimales),
    ("LotesLechones", LotesLechones),
    ("Medicamentos", Medicamentos),
    ("MonitoreoAgua", MonitoreoAgua),
    ("Movimientos", Movimientos),
    ("OrigenExterno", OrigenExterno),
    ("OrigenInterno", OrigenInterno),
    ("RegistroInseminaciones", RegistroInseminaciones),
    ("RegistroPartos", RegistroPartos),
    ("TratamientoLotes", TratamientoLotes),
    ("Tratamientos", Tratamientos),
    ("TratamientosAnimales", TratamientosAnimales),
    ("VentaLotes", VentaLotes),
    ("VentaUnidad", VentaUnidad),
]
PERMISSIONS = ['view', 'add', 'delete', 'change']

class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                model_name, model_object = model
                ct = ContentType.objects.get_for_model(model_object)
                for permission in PERMISSIONS:
                    name = 'Can {} {}'.format(permission, model_name)
                    codename = 'can_{}_{}'.format(permission, model_name)
                    print("Creating {}".format(name))
                    model_add_perm, created = Permission.objects.get_or_create(
                        codename=codename,
                        name=name,
                        content_type=ct
                    )
                    try:
                        new_group.permissions.add(model_add_perm)
                    except AttributeError as e:
                        pass

        print("Created default group and permissions.")