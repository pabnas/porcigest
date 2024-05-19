from django import forms
from django.forms import ModelChoiceField
from django.utils import timezone
from django.db.models import Q

import logging
logger = logging.getLogger(__name__)

from apps.gestion_animales.forms import InventarioAnimalesChoiceField, LotesLechonesChoiceField
from models import InventarioAnimales, LotesLechones, Medicamentos, TratamientoLotes, Tratamientos, TratamientosAnimales

class TratamientosChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.id_medicamento is not None:
            return f"Tratamiento id:{obj.id_tratamiento}/{obj.tipo_tratamiento}/{obj.id_medicamento.nombre_medicamento}"
        return f"Tratamiento id:{obj.id_tratamiento}/{obj.tipo_tratamiento}"

class MedicamentosChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Medicamento id:{obj.id_medicamento}/{obj.nombre_medicamento}/{obj.laboratorio}"

class MedicamentosForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields =[
            'nombre_medicamento',
            'principio_activo',
            'laboratorio',
            'presentacion',
            'fecha_vencimiento',
            'stock',
            'lote_medicamento',
            'vendedor_medicamento',
            'precio_unidad',
            'fecha_compra',
            'observaciones'
        ]
        
    def __init__(self, *args, **kwargs):
        super(MedicamentosForm, self).__init__(*args, **kwargs)
        
    nombre_medicamento = forms.CharField(max_length=50)
    principio_activo = forms.CharField(max_length=50)
    laboratorio = forms.CharField(max_length=50)
    presentacion = forms.CharField(max_length=50)
    fecha_vencimiento = forms.DateField(widget = forms.SelectDateWidget)
    stock = forms.IntegerField()
    lote_medicamento = forms.CharField(max_length=50)
    vendedor_medicamento = forms.CharField(max_length=50)
    precio_unidad = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = forms.DateField(widget = forms.SelectDateWidget)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)

class MedicamentosSalidaForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields =[
            'nombre_medicamento',
            'stock',
        ]
        
    def __init__(self, *args, **kwargs):
        super(MedicamentosSalidaForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        medicamento_obj = cleaned_data.get("nombre_medicamento")
        stock = cleaned_data.get("stock")
        
        if medicamento_obj and stock:
            if stock > medicamento_obj.stock:
                self.add_error('stock', f"La cantidad disponible es insuficiente. Stock disponible: {medicamento_obj.stock}")
        
        return cleaned_data
    
    current_date = timezone.now().date()
    nombre_medicamento = MedicamentosChoiceField(queryset=Medicamentos.objects.filter(fecha_vencimiento__gte=current_date))
    stock = forms.IntegerField(label='Cantidad')


class TratamientosAnimalesForm(forms.ModelForm):
    class Meta:
        model = TratamientosAnimales
        fields =[
            'id_tratamiento',
            'id_animal',
            'fecha_tratamiento_animal',
            'observaciones_animal'
        ]
        
    def __init__(self, *args, **kwargs):
        super(TratamientosAnimalesForm, self).__init__(*args, **kwargs)
    
    current_date = timezone.now().date()
    valid_tratamientos = Tratamientos.objects.filter(
        Q(id_medicamento__fecha_vencimiento__gte=current_date) | Q(id_medicamento__isnull=True)
    )
    
    id_tratamiento = TratamientosChoiceField(queryset=valid_tratamientos)
    id_animal = InventarioAnimalesChoiceField(queryset=InventarioAnimales.objects.all())
    fecha_tratamiento_animal = forms.DateField(widget = forms.SelectDateWidget)
    observaciones_animal = forms.CharField(widget=forms.Textarea, max_length=255, required=False)


class TratamientoLotesForm(forms.ModelForm):
    class Meta:
        model = TratamientoLotes
        fields =[
            'id_tratamiento',
            'id_lote',
            'fecha_aplicacion_lote',
            'dosis_lote',
            'observaciones_lote'
        ]
        
    def __init__(self, *args, **kwargs):
        super(TratamientoLotesForm, self).__init__(*args, **kwargs)
        
    current_date = timezone.now().date()
    valid_tratamientos = Tratamientos.objects.filter(
        Q(id_medicamento__fecha_vencimiento__gte=current_date) | Q(id_medicamento__isnull=True)
    )
    
    id_tratamiento = TratamientosChoiceField(queryset=valid_tratamientos)
    id_lote = LotesLechonesChoiceField(queryset=LotesLechones.objects.all())
    fecha_aplicacion_lote = forms.DateField(widget = forms.SelectDateWidget)
    dosis_lote = forms.IntegerField()
    observaciones_lote = forms.CharField(widget=forms.Textarea, max_length=255, required=False)

class TratamientosForm(forms.ModelForm):
    class Meta:
        model = Tratamientos
        fields =[
            'tipo_tratamiento',
            'detalle_tratamiento',
            'id_medicamento',
            'dosis',
            'observaciones'
        ]
        
    def __init__(self, *args, **kwargs):
        super(TratamientosForm, self).__init__(*args, **kwargs)
    
    current_date = timezone.now().date()
    
    tipo_tratamiento = forms.CharField(max_length=50)
    detalle_tratamiento = forms.CharField(max_length=255)
    id_medicamento = MedicamentosChoiceField(queryset=Medicamentos.objects.filter(fecha_vencimiento__gte=current_date))
    dosis = forms.DecimalField(max_digits=10, decimal_places=2)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)
