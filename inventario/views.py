from django.db.models import Q, Sum, F
from django.shortcuts import render
from django.conf import settings

from entradas.models import Inventario
from entradas.models import GenerarCodigoBarras
# Create your views here.

def inventario(request):
    inventario = Inventario.objects.order_by('nombre').distinct('nombre')
    b1 = Inventario.objects.values("nombre").annotate(inv_total=Sum('inventario')+ Sum('entrega'),
                            resta = Sum('inventario')- Sum('entrega')).order_by("nombre")
    context ={
        'inventario':inventario,
        'suma':b1,
    }
    return render(request, 'inventario/inventario.html',context)

