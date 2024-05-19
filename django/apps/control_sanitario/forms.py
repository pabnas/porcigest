from django import forms
from django.forms import ModelChoiceField

from models import Medicamentos


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
