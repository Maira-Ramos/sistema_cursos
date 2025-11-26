from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['curso', 'titulo', 'conteudo', 'link_video']

