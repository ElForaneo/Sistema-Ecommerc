from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Users


class RegistrarForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text="Requerido. Ingresa un id del Empleado", 
                            widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Usuario'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Ingrese contraseña'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off','placeholder':'Verifique la contraseña'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese Email'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su Nombre'}))
    apellido_paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su primer Apellido'}))
    apellido_materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su segundo Apellido'}))
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'onkeypress':'phoneNumberFormatter()','type':'text','id':'phone','placeholder':'(123) 456 7890','class':'form-control'}))
    is_staff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input','id':'flexSwitchCheckDefault','type':'checkbox','role':'switch'}))
    
    class Meta:
        model = Users
        fields = ("id","username","email","nombre","apellido_paterno","apellido_materno","telefono","local","is_staff","password1","password2")

class EditarUsuarioForm(UserChangeForm):
    username = forms.CharField(max_length=20, help_text="Requerido. Ingresa un id del Empleado", 
                            widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese Usuario'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese Email'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su Nombre'}))
    apellido_paterno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su primer Apellido'}))
    apellido_materno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su segundo Apellido'}))
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'onkeypress':'phoneNumberFormatter()','type':'text','id':'phone','placeholder':'(123) 456 7890','class':'form-control'}))
    local = forms.CharField
    is_staff = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input','id':'flexSwitchCheckDefault','type':'checkbox','role':'switch'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input','id':'flexSwitchCheckDefaults','type':'checkbox','role':'switch'}))
    
    class Meta:
        model = Users
        fields = ("id","username","email","nombre","apellido_paterno","apellido_materno","telefono","local","is_staff","is_active")