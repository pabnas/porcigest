from django import forms
from django.forms import ModelChoiceField
from django.utils import timezone

from apps.gestion_animales.forms import InventarioAnimalesChoiceField, LotesLechonesChoiceField
from models import InventarioAnimales, LotesLechones, Medicamentos, TratamientoLotes, Tratamientos, TratamientosAnimales

class TratamientosChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.id_medicamento is not None:
            return f"Tratamiento {obj.tipo_tratamiento}/{obj.id_medicamento.nombre_medicamento}"
        return f"Tratamiento {obj.tipo_tratamiento}"

class MedicamentosChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"Medicamento {obj.nombre_medicamento}/{obj.laboratorio}"

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
            'laboratorio',
            'presentacion',
            'stock',
        ]
        
    def __init__(self, *args, **kwargs):
        super(MedicamentosSalidaForm, self).__init__(*args, **kwargs)
    
    nombre_medicamento = forms.CharField(max_length=50)
    laboratorio = forms.CharField(max_length=50)
    presentacion = forms.CharField(max_length=50)
    stock = forms.IntegerField()


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
        
    id_tratamiento = TratamientosChoiceField(queryset=Tratamientos.objects.all())
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
    
    id_tratamiento = TratamientosChoiceField(queryset=Tratamientos.objects.all())
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
