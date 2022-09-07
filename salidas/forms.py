from django import forms

from entradas.models import Inventario

class SalidaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    almacen = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    salida = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Inventario
        fields = ['nombre','almacen','salida','estado']
