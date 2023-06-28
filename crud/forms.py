from django import forms
from django.forms import ModelForm
from .models import *

class JoyeriaForm(ModelForm):
    class Meta:
        model = Joyeria
        fields = [
            'idJoyeria',
            'name',
            'marca',
            'tipo',
            'value',
            'stock',
            'image'
        ]
        labels = {
            'idJoyeria':'ID',
            'name':'Nombre',
            'marca':'Marca',
            'tipo':'Tipo de Joyeria',
            'value':'Valor',
            'stock':'Stock',
            'image':'Imagen'
        }
        widgets = {
            'idJoyeria':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.Select(attrs={'class':'form-control'}),
            'value':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class MarcaForm(ModelForm):
    pass