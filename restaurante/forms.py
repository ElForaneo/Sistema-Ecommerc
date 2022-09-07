from django import forms

from .models import locales
from .models import Platillos

class PlatillosForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escriba el nombre del platillo'}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Costo del platillo'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholer':'Una descripcion breve del producto'}))
    class Meta:
        model = Platillos
        fields = ['nombre','precio','descripcion','img_platillo']

class LocalesForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe el nombre distintivo del local'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion del local'}))
    cp = forms.CharField(widget=forms.NumberInput(attrs={'class':'forms-control','placeholder':' Ingrese el Codigo Postal'}))
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'onkeypress':'phoneNumberFormatter()','type':'text','id':'phone','placeholder':'(123) 456 7890','class':'form-control'}))
    class Meta:
        model = locales
        fields = ['nombre','direccion','cp','telefono']