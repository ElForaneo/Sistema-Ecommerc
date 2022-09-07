from django.contrib import admin
from django.db import models

# Create your models here.

class Almacenes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=True,null=False)
    direccion = models.CharField(max_length=200,blank=True,null=False)
    cp = models.CharField(max_length=10,blank=True,null=False)
    telefono = models.CharField(max_length=16,blank=True,null=False)
    date_creado = models.DateTimeField(verbose_name='Fecha creado',auto_now_add=True)
    date_modificado = models.DateTimeField(verbose_name='Ultima modificacion',auto_now=True)

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','cp','telefono')