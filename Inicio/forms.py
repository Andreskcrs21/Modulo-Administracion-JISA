from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name' : 'Nombres',
            'last_name' : 'Apellidos',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar Contraseña'

        } 
        help_texts = {k:"" for k in fields           
        }