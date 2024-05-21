from django import forms
from django.forms import ModelChoiceField
from models import IngresoVehiculos

class TimePickerInput(forms.TimeInput):
        input_type = 'time'
        
class DatePickerInput(forms.DateInput):
        input_type = 'date'


class IngresoVehiculosForm(forms.ModelForm):
    class Meta:
        model = IngresoVehiculos
        fields =[
            'fecha_ingreso',
            'hora_ingreso',
            'placa_vehiculo',
            'nombre_conductor',
            'nombres_acompanantes',
            'telefono_conductor',
            'empresa_transportista',
            'tipo_vehiculo',
            'motivo_ingreso',
            'ultimo_predio_visitado',
            'observaciones'
        ]
        
    def __init__(self, *args, **kwargs):
        super(IngresoVehiculosForm, self).__init__(*args, **kwargs)
    
    fecha_ingreso = forms.DateField(widget = DatePickerInput)
    hora_ingreso = forms.TimeField(widget = TimePickerInput)
    placa_vehiculo = forms.CharField(max_length=20)
    nombre_conductor = forms.CharField(max_length=50)
    nombres_acompanantes = forms.CharField(max_length=255, required=False)
    telefono_conductor = forms.CharField(max_length=20, required=False)
    empresa_transportista = forms.CharField(max_length=100, required=False)
    tipo_vehiculo = forms.CharField(max_length=50)
    motivo_ingreso = forms.CharField(max_length=255)
    ultimo_predio_visitado = forms.CharField(max_length=100, required=False)
    observaciones = forms.CharField(widget=forms.Textarea, max_length=255, required=False)
