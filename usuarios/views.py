from .models import Users
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrarForm, EditarUsuarioForm
# Create your views here.

def PaginaLogin(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'El usuario es incorrecto o no existe, verifique porfavor')
                return render(request,'cuentas/login.html',context)
        context = {}
        return render(request,'cuentas/login.html',context)    

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def PaginaRegistrar(request):
    form = RegistrarForm()
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('usuario')
        
    context = {'form':form}
    return render(request, 'cuentas/registrar.html', context)

def EditarUsuario(request,pk):
    usuarios = Users.objects.all
    usuario = Users.objects.get(id=pk)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    
    form = EditarUsuarioForm(instance = usuario)
    context={'form':form,'usuarios':usuarios}
    return render(request, 'lista_cuentas/editar_cuentas.html', context)

def BorrarUsuario(request,pk):
    usuario = Users.objects.get(id=pk)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario')

    context={'usaurio':usuario}
    return render(request, 'lista_cuentas/borrarusauriomodal.html', context)


@login_required(login_url='login')
def usuario(request):
    usuarios = Users.objects.exclude(is_admin=True) & Users.objects.exclude(is_superuser=True)
    
    
    return render(request, 'lista_cuentas/cuentas.html',{'usuarios':usuarios,'local':'local'})