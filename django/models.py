# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Corrales(models.Model):
    num_corral = models.IntegerField(primary_key=True)
    id_area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    aforo = models.IntegerField()
    cantidad_dentro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'corrales'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IngresoVehiculos(models.Model):
    id_ingreso_vehiculo = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    placa_vehiculo = models.CharField(unique=True, max_length=20)
    nombre_conductor = models.CharField(max_length=50)
    telefono_conductor = models.CharField(max_length=20, blank=True, null=True)
    empresa_transportista = models.CharField(max_length=50)
    tipo_vehiculo = models.CharField(max_length=50)
    motivo_ingreso = models.CharField(max_length=255)
    ultimo_predio_visitado = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso_vehiculos'


class InventarioAnimales(models.Model):
    id_animal = models.AutoField(primary_key=True)
    id_corral = models.ForeignKey(Corrales, models.DO_NOTHING, db_column='id_corral')
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    estado_salud = models.CharField(max_length=50)
    origen = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'inventario_animales'


class LotesLechones(models.Model):
    id_lote = models.AutoField(primary_key=True)
    id_corral = models.ForeignKey(Corrales, models.DO_NOTHING, db_column='id_corral')
    cantidad_lechones = models.IntegerField()
    fecha_ingreso_lote = models.DateField()
    dias_precebo = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotes_lechones'


class LotesTratamientos(models.Model):
    id_lote_tratamiento = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey('Tratamientos', models.DO_NOTHING, db_column='id_tratamiento')
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote')
    fecha_aplicacion_lote = models.DateField()
    dosis_lote = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones_lote = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotes_tratamientos'


class Medicamentos(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=50)
    principio_activo = models.CharField(max_length=50)
    laboratorio = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    stock = models.IntegerField()
    lote_medicamento = models.CharField(max_length=50, blank=True, null=True)
    vendedor_medicamento = models.CharField(max_length=50, blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamentos'


class MonitoreoAgua(models.Model):
    id_monitoreo = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField()
    nivel_agua_porcentaje = models.DecimalField(max_digits=3, decimal_places=1)
    flujo_agua_litros_hora = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'monitoreo_agua'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha = models.DateField()
    area_origen = models.ForeignKey(Areas, models.DO_NOTHING, db_column='area_origen')
    area_destino = models.ForeignKey(Areas, models.DO_NOTHING, db_column='area_destino', related_name='movimientos_area_destino_set')

    class Meta:
        managed = False
        db_table = 'movimientos'


class OrigenExterno(models.Model):
    id_origen_externo = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_compra = models.DateField()
    fecha_ingreso = models.DateField()
    finalidad_compra = models.CharField(max_length=50)
    etapa_productiva = models.CharField(max_length=50)
    granja_origen = models.CharField(max_length=255)
    edad = models.IntegerField()
    vendedor = models.CharField(max_length=255, blank=True, null=True)
    peso_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'origen_externo'


class OrigenInterno(models.Model):
    id_origen_interno = models.AutoField(primary_key=True)
    fecha_cambio_etapa = models.DateField()
    finalidad = models.CharField(max_length=50)
    etapa_productiva = models.CharField(max_length=50)
    id_madre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_madre')
    id_padre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_padre', related_name='origeninterno_id_padre_set', blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'origen_interno'


class RegistroInseminaciones(models.Model):
    id_inseminacion = models.AutoField(primary_key=True)
    id_madre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_madre')
    id_padre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_padre', related_name='registroinseminaciones_id_padre_set', blank=True, null=True)
    fecha_inseminacion = models.DateField()
    tipo_inseminacion = models.CharField(max_length=2)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_inseminaciones'


class RegistroPartos(models.Model):
    id_parto = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_parto = models.DateField()
    nacidos_vivos = models.IntegerField()
    nacidos_muertos = models.IntegerField()
    vivos_48h = models.IntegerField()
    vivos_destete = models.IntegerField()
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_partos'


class Tratamientos(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    tipo_tratamiento = models.CharField(max_length=50)
    detalle_tratamiento = models.CharField(max_length=255)
    id_medicamento = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamientos'


class TratamientosAnimales(models.Model):
    id_tratamiento_animal = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey(Tratamientos, models.DO_NOTHING, db_column='id_tratamiento')
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_tratamiento_animal = models.DateField()
    observaciones_animal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamientos_animales'


class VentaLotes(models.Model):
    id_venta_lotes = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote')
    peso_promedio = models.DecimalField(max_digits=5, decimal_places=2)
    precio_lote = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=50)
    comprador = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_lotes'


class VentaUnidad(models.Model):
    id_venta_unidad = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote')
    peso_lechon = models.DecimalField(max_digits=5, decimal_places=2)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=50)
    comprador = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_unidad'
