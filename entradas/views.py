from django.shortcuts import render, redirect
from .models import GenerarCodigoBarras, Inventario
from .forms import GenerarCBForm
from .forms import ProductoFrom, EditarProductoForm


# Create your views here.

def entradas(request):
    codigo_barras = GenerarCodigoBarras.objects.all
    productos = Inventario.objects.all
    context={
        'codigo_barras': codigo_barras,
        'productos': productos,
        }
    return render(request,'entradas/entradas.html',context)

def Crearentradas(request):
    form = GenerarCBForm
    if request.method == 'POST':
        form = GenerarCBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entradas')
    context={
        'form':form
        }
    return render(request,'entradas/crear_entradas.html',context)

def Crearproducto(request):
    productos = GenerarCodigoBarras.objects.all()
    formEntra = ProductoFrom
    if request.method == 'POST':
        formEntra = ProductoFrom(request.POST, request.FILES)
        if formEntra.is_valid():
            formEntra.save()
            return redirect('entradas')
    context = {
        'formEntra':formEntra,
        'productos': productos,
        }
    return render(request,'entradas/crear_producto.html',context)

def EditarProducto(request,pk):
    producto = Inventario.objects.get(id=pk)
    if request.method == 'POST':
        form = EditarProductoForm(request.POST,instance = producto)
        if form.is_valid():
            form.save()
            return redirect('entradas')
    form = EditarProductoForm(instance=producto)
    context={
        'form':form,
    }
    return render(request,'entradas/editar_entradas.html',context)

def BorrarProducto(request,pk):
    delproducto = Inventario.objects.get(id=pk)
    if request.method == 'POST':
        delproducto.delete()
        return redirect('entradas')
    context={
        'delproducto':delproducto
    }
    return render(request,'entradas/borrar_productos.html',context)
