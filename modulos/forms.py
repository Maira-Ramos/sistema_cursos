from django import forms
from .models import Modulo
from cursos.models import Curso

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ["curso", "nome", "descricao"]

        widgets = {
            "curso": forms.Select(attrs={"class": "form-select"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
