# modulos/forms.py

from django import forms
from .models import Modulo

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nome', 'descricao', 'curso']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do módulo'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do módulo'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
        }
