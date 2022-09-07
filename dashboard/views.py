from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html',{})


def calendario(request):
    return render(request, 'dashboard/calendario.html',{})

def salida(request):
    return render(request, 'dashboard/salida.html',{})

