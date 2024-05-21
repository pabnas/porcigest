from django import forms
from django.forms import ModelChoiceField

from models import Areas, Corrales, InventarioAnimales, LotesLechones, Movimientos, OrigenExterno, OrigenInterno, VentaUnidad
from models import RegistroInseminaciones, RegistroPartos, VentaLotes

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class InventarioAnimalesChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Animal #:{obj.numero_identificacion_animal}"

class CorralesChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Corral #{obj.num_corral}"
    
class LotesLechonesChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Lote lechones id:{obj.id_lote}"

class AreasChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Area id:{obj.id_area}"
    
TIPO_INSEMINACION = [
    # TEXT, VALUE
    ('MN', 'Monta Natural'),
    ('IA', 'Inseminación Artificial'),
    ('TE', 'Transferencia de Embriones'),
    ('O', 'Otros (Especificar en observaciones)')
]

TIPO_SEXO = [
    # TEXT, VALUE
    ('M', 'Macho'),
    ('F', 'Hembra'),
]


TIPO_ORIGEN = [
    # TEXT, VALUE
    ('', 'Seleccione una opción'),
    ('I', 'Interno'),
    ('E', 'Externo'),
]

TIPO_ESTADO_PRODUCTIVO = [
    # TEXT, VALUE
    ('lactancia', 'lactancia'),
    ('gestacion', 'gestacion'),
    ('remplazo', 'remplazo'),
    ('engorde', 'engorde'),
    ('vendido', 'vendido'),
]


class RegistroInseminacionesForm(forms.ModelForm):
    class Meta:
        model = RegistroInseminaciones
        fields =[
            'id_madre',
            'id_padre',
            'fecha_inseminacion',
            'tipo_inseminacion',
            'observaciones'
        ]
        
    def __init__(self, *args, **kwargs):
        super(RegistroInseminacionesForm, self).__init__(*args, **kwargs)

    id_madre = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.filter(sexo='H'))
    id_padre = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.filter(sexo='M'), required=False, blank=True)
    fecha_inseminacion = forms.DateField(widget = DatePickerInput)
    tipo_inseminacion = forms.ChoiceField(choices=TIPO_INSEMINACION)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False) 


class RegistroPartosForm(forms.ModelForm):
    class Meta:
        model = RegistroPartos
        fields =[
            'id_animal',
            'fecha_parto',
            'nacidos_vivos',
            'nacidos_muertos',
            'vivos_48h',
            'vivos_destete',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(RegistroPartosForm, self).__init__(*args, **kwargs)
    
    id_animal = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.filter(sexo='H'))
    fecha_parto = forms.DateField(widget = DatePickerInput)
    nacidos_vivos = forms.IntegerField()
    nacidos_muertos = forms.IntegerField()
    vivos_48h = forms.IntegerField(required=False)
    vivos_destete = forms.IntegerField(required=False)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)

class LotesLechonesForm(forms.ModelForm):
    class Meta:
        model = LotesLechones
        fields =[
            'id_corral',
            'cantidad_lechones',
            'fecha_ingreso_lote',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(LotesLechonesForm, self).__init__(*args, **kwargs)
    
    id_corral = CorralesChoiceField(queryset=Corrales.objects.all())
    cantidad_lechones = forms.IntegerField()
    fecha_ingreso_lote = forms.DateField(widget = DatePickerInput)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)


class VentaLotesForm(forms.ModelForm):
    class Meta:
        model = VentaLotes
        fields =[
            'fecha_venta',
            'id_lote',
            'peso_promedio',
            'precio_lote',
            'destino',
            'comprador',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(VentaLotesForm, self).__init__(*args, **kwargs)
    
    fecha_venta = forms.DateField(widget = DatePickerInput)
    id_lote = LotesLechonesChoiceField(queryset=LotesLechones.objects.all())
    peso_promedio = forms.DecimalField(max_digits=5, decimal_places=2)
    precio_lote = forms.DecimalField(max_digits=10, decimal_places=2)
    destino = forms.CharField(max_length=50, required=False)
    comprador = forms.CharField(max_length=255)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)


class MovimientosForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        fields =[
            'id_animal',
            'fecha',
            'area_origen',
            'area_destino',
        ]
        
    def __init__(self, *args, **kwargs):
        super(MovimientosForm, self).__init__(*args, **kwargs)

    id_animal = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.all())
    fecha = forms.DateField(widget = DatePickerInput)
    area_origen = AreasChoiceField(queryset=Areas.objects.all())
    area_destino = AreasChoiceField(queryset=Areas.objects.all())


class OrigenInternoForm(forms.ModelForm):
    class Meta:
        model = OrigenInterno
        fields =[
            'fecha_cambio_etapa',
            'finalidad',
            'etapa_productiva_ingreso',
            'id_madre',
            'id_padre',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(OrigenInternoForm, self).__init__(*args, **kwargs)
    
    fecha_cambio_etapa = forms.DateField(widget = DatePickerInput)
    finalidad = forms.CharField(max_length=50)
    etapa_productiva_ingreso = forms.CharField(max_length=50)
    id_madre = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.filter(sexo='H'))
    id_padre = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.filter(sexo='M'), required=False, blank=True)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)
    
    
class OrigenExternoForm(forms.ModelForm):
    class Meta:
        model = OrigenExterno
        fields =[
            'fecha_compra',
            'fecha_ingreso',
            'finalidad_compra',
            'etapa_productiva_ingreso',
            'vendedor',
            'peso_compra',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(OrigenExternoForm, self).__init__(*args, **kwargs)
    
    fecha_compra = forms.DateField(widget = DatePickerInput)
    fecha_ingreso = forms.DateField(widget = DatePickerInput)
    finalidad_compra = forms.CharField(max_length=50)
    etapa_productiva_ingreso = forms.CharField(max_length=50)
    vendedor = forms.CharField(max_length=255)
    peso_compra = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)


class InventarioAnimalesForm(forms.ModelForm):
    class Meta:
        model = InventarioAnimales
        fields =[
            'numero_identificacion_animal',
            'id_corral',
            'raza',
            'sexo',
            'edad',
            'peso',
            'estado_productivo',
            'origen',
        ]
        
    def __init__(self, *args, **kwargs):
        super(InventarioAnimalesForm, self).__init__(*args, **kwargs)
    
    def customSave(self):
        lv = self.save(commit=False)
        lv.save()
        return lv
    
    numero_identificacion_animal = forms.CharField(max_length=50)
    id_corral = CorralesChoiceField(queryset=Corrales.objects.all())
    raza = forms.CharField(max_length=50)
    sexo = forms.ChoiceField(choices=TIPO_SEXO)
    edad = forms.IntegerField()
    peso = forms.DecimalField(max_digits=10, decimal_places=2)
    estado_productivo = forms.ChoiceField(choices=TIPO_ESTADO_PRODUCTIVO)
    origen = forms.ChoiceField(choices=TIPO_ORIGEN)
    origen_interno = OrigenInternoForm(prefix="origen_interno")
    origen_externo = OrigenExternoForm(prefix="origen_externo")

class VentaUnidadForm(forms.ModelForm):
    class Meta:
        model = VentaUnidad
        fields =[
            'fecha_venta',
            'id_lote',
            'id_animal',
            'peso',
            'precio_unidad',
            'destino',
            'comprador',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(VentaUnidadForm, self).__init__(*args, **kwargs)
    
    fecha_venta = forms.DateField(widget = DatePickerInput)
    id_lote = LotesLechonesChoiceField(queryset=LotesLechones.objects.all(), required=False)
    id_animal = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.all(), required=False)
    peso = forms.DecimalField(max_digits=5, decimal_places=2)
    precio_unidad = forms.DecimalField(max_digits=10, decimal_places=2)
    destino = forms.CharField(max_length=50, required=False)
    comprador = forms.CharField(max_length=255)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)
    