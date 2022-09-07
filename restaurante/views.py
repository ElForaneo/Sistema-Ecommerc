from django.shortcuts import render,redirect
from .forms import PlatillosForm, LocalesForm
from .models import Platillos
from .models import locales
# Create your views here.


def restaurante(request):
    platillos = Platillos.objects.all
    local = locales.objects.all

    context= {
        'platillos': platillos,
        'locales': local
    }
    return render(request, 'restaurante/restaurante.html',context)

def crearplatillos(request):
    form =PlatillosForm
    if request.method == 'POST':
        form = PlatillosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurante')
    context = {'form': form}
    return render(request, 'restaurante/registrar_platillos.html',context)

def crearlocal(request):
    form = LocalesForm
    if request.method == 'POST':
        form = LocalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurante')
    context = {'form':form}
    return render(request,'restaurante/registrar_local.html',context)