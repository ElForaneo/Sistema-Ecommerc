from django.shortcuts import render, redirect

from .forms import SalidaForm
# Create your views here.

def salidas_lista(request):

    context={

    }

    return render(request,'salidas/salidas.html',context)

def salidas_add(request):
    form = SalidaForm()
    if request.method == 'POST':
        form = SalidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
        
    context = {
        'form':form,
    }
    return render(request, 'salidas/salidas_add.html', context)

