from pyexpat import model
from django import forms

from .models import cortecaja
from .models import orden

class CorteCajaForm(forms.ModeForm):
    id = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = cortecaja
        fields = ['id' ,'usuario','platillos','Nd_caja','MontoInicial','MontoDCierre','Fecha_apertura','Hora_apertura','Fecha_cierre']