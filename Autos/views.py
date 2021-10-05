from django.shortcuts import render, redirect
from .forms import AutosForm, MotoForm
from Autos.models import*
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.

def registro_autos(request):
    if request.method == 'GET':
        form = AutosForm
        contexto = {
        'form' : form
        }
    else:
        form = AutosForm(request.POST, request.FILES)
        contexto = {
        'form' : form
        }
        if form.is_valid():
               form.save()
               return redirect('autos:lista_autos')
    return render(request,  "carros/registro_autos.html", contexto)

def lista_autos(request):
    busqueda = request.GET.get("buscar")
    autos = Auto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(autos, 6)
        autos = paginator.page(page)

    except:
        raise Http404

    if busqueda:
        autos = Auto.objects.filter(
            Q(Marca__icontains = busqueda) | 
            Q(Modelo__icontains = busqueda)
        ).distinct()
    return render(request, 'carros/lista_autos.html', {"entity":autos, "paginator" : paginator})

def editarAuto(request,id):
    auto = Auto.objects.get(id = id)
    if request.method == 'GET':
        form = AutosForm(instance= auto)
        contexto = {
            'form': form
        }
    else:
        form = AutosForm(request.POST, request.FILES, instance= auto)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('autos:lista_autos')            
    return render(request,  "carros/registro_autos.html", contexto)


def eliminarAuto(request,id):
    auto = Auto.objects.get(id = id)
    auto.delete()
    return redirect('autos:lista_autos')            

# View Motos

def registro_moto(request):
    if request.method == 'GET':
        form = MotoForm
        contexto = {
        'form' : form
        }
    else:
        form = MotoForm(request.POST, request.FILES)
        contexto = {
        'form' : form
        }
        if form.is_valid():
               form.save()
               return redirect('autos:lista_motos')
    return render(request,  "carros/registro_moto.html", contexto)

def lista_moto(request):
    busqueda = request.GET.get("buscar")
    motos = Moto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(motos, 6)
        motos = paginator.page(page)

    except:
        raise Http404

    if busqueda:
        motos = Moto.objects.filter(
            Q(Marca__icontains = busqueda) | 
            Q(Modelo__icontains = busqueda)
        ).distinct()
    return render(request, 'carros/lista_motos.html',{"entity":motos, "paginator": paginator})

def editarMoto(request,id):
    moto = Moto.objects.get(id = id)
    if request.method == 'GET':
        form = MotoForm(instance= moto)
        contexto = {
            'form': form
        }
    else:
        form = MotoForm(request.POST, request.FILES, instance= moto)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('autos:lista_motos')            
    return render(request,  "carros/registro_moto.html", contexto)


def eliminarMoto(request,id):
    moto = Moto.objects.get(id = id)
    moto.delete()
    return redirect('autos:lista_motos')   