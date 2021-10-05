from django import forms
from .models import Auto, Moto
from Autos import models

class AutosForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'