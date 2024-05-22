import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from models import Medicamentos, TratamientosAnimales, TratamientoLotes, Tratamientos

GROUPS = ['veterinario']
MODELS = [
    ('Medicamentos', Medicamentos),
    ('TratamientosAnimales', TratamientosAnimales),
    ('TratamientoLotes', TratamientoLotes),
    ('Tratamientos', Tratamientos)
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
                    try:
                        model_add_perm = Permission.objects.create(
                            codename=codename,
                            name=name,
                            content_type=ct
                        )
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue
                    new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")