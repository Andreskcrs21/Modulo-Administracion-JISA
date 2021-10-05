from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistroForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Autos.models import Auto, Moto

def registro(request):
    contexto = {
        'form' : RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'El usuario {user} se ha creado')
            return redirect('inicio:inicio')
        contexto["form"] = formulario
    return render(request, "login/registro.html", contexto)

def inicio(request):
    return render(request, "login/inicio.html", {"autos":Auto.objects.all , "motos":Moto.objects.all})

def bienvenida(request):
    return render(request, "login/bienvenida.html")

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect(request, "inicio:bienvenida")