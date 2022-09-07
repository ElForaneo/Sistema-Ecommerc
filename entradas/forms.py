from django import forms

from .models import GenerarCodigoBarras
from .models import Inventario

class GenerarCBForm(forms.ModelForm):
    nombre = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre del producto'}))
    codigo_barras = forms.CharField(max_length=13,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el codigo de barras'}))
    
    class Meta:
        model = GenerarCodigoBarras
        fields = ['nombre','codigo_barras']


class ProductoFrom(forms.ModelForm):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre del producto'}))
    class Meta:
        model = Inventario
        fields = ['nombre','entrega','seleccion_cb','categoria','descripcion','Img_producto','estado','almacen']

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre','seleccion_cb','entrega','categoria','descripcion','Img_producto','estado']