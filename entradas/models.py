import barcode
from io import BytesIO
from django.db import models
from django.contrib import admin
from django.core.files import File
from barcode.writer import ImageWriter
from django.forms import CharField

from inventario.models import Almacenes

class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20,blank=True,null=False,unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Create your models here.
class GenerarCodigoBarras(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20,blank=True,null=False,unique=True)
    codigo_barras = models.CharField(max_length=13,blank=True,null=False)
    barcode = models.ImageField(upload_to='images/',blank=True)
       
    class Meta:
        verbose_name = 'Codigo de barra'
        verbose_name_plural = 'Codigos de barras'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre

    def save(self,*args,**kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.codigo_barras}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.nombre}-{self.codigo_barras}.png',File(buffer),save=False)
        return super().save(*args,**kwargs)

    def codigocompleto(self):
        return str(self.codigo_barras)
                
class BarcodeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigocompleto','barcode')



class Inventario(models.Model):
    ESTADO_SALIDA = [
        ('pedido','Pedido'),
        ('aceptado','Aceptado'),
        ('cancelado','Cancelado'),
        ('enviado','Enviado'),
        ('Entregado','Entregado'),
    ]

    id = models.AutoField(primary_key=True)
    Img_producto = models.ImageField(upload_to='images/producto',blank=True,null=True)
    nombre = models.CharField(max_length= 50, blank=True,null=False,unique=False)
    categoria = models.ForeignKey(categoria, default=False , on_delete=models.DO_NOTHING)
    descripcion = models.CharField(max_length=499,blank=True,null=False)
    entrega = models.PositiveIntegerField(default=0)
    precio = models.PositiveIntegerField(default=0)
    inventario = models.PositiveIntegerField(default=0)
    salida = models.PositiveBigIntegerField(default=0)
    almacen = models.ForeignKey(Almacenes,default=False,blank=True,null=True,on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=10,choices=ESTADO_SALIDA, default=False,null=False, blank=True)
    seleccion_cb = models.ForeignKey(GenerarCodigoBarras,blank=True,null=True,on_delete=models.DO_NOTHING)
    date_creado = models.DateTimeField(verbose_name='Fecha creado',auto_now_add=True)
    date_cambiado = models.DateTimeField(verbose_name='Fehca modificada',auto_now=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['date_creado']


    def __str__(self):
        return self.nombre

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'entrega')