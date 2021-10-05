
from django.shortcuts import render, redirect
from .forms import ClientesForm
from Clientes.models import*
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.

def registro_clientes(request):
    if request.method == 'GET':
        form = ClientesForm
        contexto = {
        'form' : form
        }
    else:
        form = ClientesForm(request.POST)
        contexto = {
        'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')
    return render(request, 'clientes/registro_clientes.html', contexto)

def lista_clientes(request):
    busqueda = request.GET.get("buscar")
    clientes = Clientes.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(clientes, 2)
        clientes = paginator.page(page)

    except:
        raise Http404

    if busqueda:
        clientes = Clientes.objects.filter(
            Q(Nombres__icontains = busqueda) | 
            Q(Apellidos__icontains = busqueda) |
            Q(Direccion__icontains = busqueda) | 
            Q(Telefono__icontains = busqueda) | 
            Q(Correo__icontains = busqueda) |
            Q(Cedula__icontains = busqueda) | 
            Q(Fecha_Nacimiento__icontains = busqueda) 
        ).distinct()
    return render(request, 'clientes/lista_clientes.html', {"entity":clientes, "paginator" : paginator})

def editar_cliente(request,id):
    cliente = Clientes.objects.get(id = id)
    if request.method == 'GET':
        form = ClientesForm(instance= cliente)
        contexto = {
            'form': form
        }
    else:
        form = ClientesForm(request.POST, instance= cliente)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('clientes:lista_clientes')
    return render(request, 'clientes/registro_clientes.html', contexto)

def eliminar_cliente(request,id):
    cliente = Clientes.objects.get(id = id)
    cliente.delete()
    return redirect('clientes:lista_clientes')