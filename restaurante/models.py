from django.contrib import admin
from django.db import models

# Create your models here.

class Platillos(models.Model):
    id =  models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=50, blank=True, null=False,unique=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2 , blank=True, null=False)
    descripcion = models.TextField(max_length=500,blank=True,null=False)
    img_platillo = models.ImageField(upload_to='images/platillos',blank=True)

    class Meta:
        verbose_name = 'Platillo'
        verbose_name_plural = 'Platillos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

    def preciovista(self):
        return "$ " + str(self.precio) 


class PlatillosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','preciovista','img_platillo')

class locales(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=50,blank=True,null=False,unique=True)
    direccion = models.CharField(max_length=200,blank=True,null=False)
    cp = models.CharField(max_length=10,blank=True,null=False)
    telefono = models.CharField(max_length=16,blank=True,null=False)
    date_creado = models.DateTimeField(verbose_name='Fecha creado',auto_now_add=True)
    date_modificado = models.DateTimeField(verbose_name='Ultima modificacion',auto_now=True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class LocalesAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','cp','telefono')