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
        app_label = 'gestion_animales'
        managed = False
        db_table = 'areas'


class Corrales(models.Model):
    corral_id = models.AutoField(primary_key=True)
    num_corral = models.IntegerField()
    id_area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    aforo = models.IntegerField()
    estado = models.CharField(max_length=15)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'corrales'


class IngresoVehiculos(models.Model):
    id_ingreso_vehiculo = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    placa_vehiculo = models.CharField(unique=True, max_length=20)
    nombre_conductor = models.CharField(max_length=50)
    nombres_acompanantes = models.CharField(max_length=255, blank=True, null=True)
    telefono_conductor = models.CharField(max_length=20, blank=True, null=True)
    empresa_transportista = models.CharField(max_length=100, blank=True, null=True)
    tipo_vehiculo = models.CharField(max_length=50)
    motivo_ingreso = models.CharField(max_length=255)
    ultimo_predio_visitado = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'ingreso_vehiculos'


class InventarioAnimales(models.Model):
    id_animal = models.AutoField(primary_key=True)
    numero_identificacion_animal = models.CharField(max_length=50)
    id_corral = models.ForeignKey(Corrales, models.DO_NOTHING, db_column='id_corral')
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    estado_productivo = models.CharField(max_length=50)
    origen = models.CharField(max_length=1)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'inventario_animales'


class LotesLechones(models.Model):
    id_lote = models.AutoField(primary_key=True)
    id_corral = models.ForeignKey(Corrales, models.DO_NOTHING, db_column='id_corral')
    cantidad_lechones = models.IntegerField()
    fecha_ingreso_lote = models.DateField()
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'lotes_lechones'


class Medicamentos(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=200)
    fecha_vencimiento = models.DateField()
    stock = models.IntegerField()
    lote_medicamento = models.CharField(max_length=50, blank=True, null=True)
    vendedor_medicamento = models.CharField(max_length=255, blank=True, null=True)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'medicamentos'


class MonitoreoAgua(models.Model):
    id_monitoreo = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField()
    nivel_agua_porcentaje = models.DecimalField(max_digits=3, decimal_places=1)
    flujo_agua_litros_hora = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'monitoreo_agua'


class Movimientos(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha = models.DateField()
    area_origen = models.ForeignKey(Areas, models.DO_NOTHING, db_column='area_origen')
    area_destino = models.ForeignKey(Areas, models.DO_NOTHING, db_column='area_destino', related_name='movimientos_area_destino_set')

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'movimientos'


class OrigenExterno(models.Model):
    id_origen_externo = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_compra = models.DateField()
    fecha_ingreso = models.DateField()
    finalidad_compra = models.CharField(max_length=50)
    etapa_productiva_ingreso = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=255)
    peso_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'origen_externo'


class OrigenInterno(models.Model):
    id_origen_interno = models.AutoField(primary_key=True)
    fecha_cambio_etapa = models.DateField()
    finalidad = models.CharField(max_length=50)
    etapa_productiva_ingreso = models.CharField(max_length=50)
    id_madre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_madre')
    id_padre = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_padre', related_name='origeninterno_id_padre_set', blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
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
        app_label = 'gestion_animales'
        managed = False
        db_table = 'registro_inseminaciones'

class RegistroPartos(models.Model):
    id_parto = models.AutoField(primary_key=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_parto = models.DateField()
    nacidos_vivos = models.IntegerField()
    nacidos_muertos = models.IntegerField()
    vivos_48h = models.IntegerField(blank=True, null=True)
    vivos_destete = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'registro_partos'


class TratamientoLotes(models.Model):
    id_lote_tratamiento = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey('Tratamientos', models.DO_NOTHING, db_column='id_tratamiento')
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote')
    fecha_aplicacion_lote = models.DateField()
    dosis_lote = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones_lote = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'tratamiento_lotes'


class Tratamientos(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    tipo_tratamiento = models.CharField(max_length=50)
    detalle_tratamiento = models.CharField(max_length=255)
    id_medicamento = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'tratamientos'


class TratamientosAnimales(models.Model):
    id_tratamiento_animal = models.AutoField(primary_key=True)
    id_tratamiento = models.ForeignKey(Tratamientos, models.DO_NOTHING, db_column='id_tratamiento')
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal')
    fecha_tratamiento_animal = models.DateField()
    observaciones_animal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'tratamientos_animales'


class VentaLotes(models.Model):
    id_venta_lotes = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote')
    peso_promedio = models.DecimalField(max_digits=5, decimal_places=2)
    precio_lote = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=50, blank=True, null=True)
    comprador = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'venta_lotes'


class VentaUnidad(models.Model):
    id_venta_unidad = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    id_lote = models.ForeignKey(LotesLechones, models.DO_NOTHING, db_column='id_lote', blank=True, null=True)
    id_animal = models.ForeignKey(InventarioAnimales, models.DO_NOTHING, db_column='id_animal', blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=50, blank=True, null=True)
    comprador = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gestion_animales'
        managed = False
        db_table = 'venta_unidad'
