from django import forms
from .models import Aula
from cursos.models import Curso
from modulos.models import Modulo  # <- CORRETO





class AulaForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)
    modulo = forms.ModelChoiceField(queryset=Modulo.objects.none(), required=True)

    class Meta:
        model = Aula
        fields = ['curso', 'modulo', 'titulo', 'conteudo', 'link_video']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['modulo'].queryset = Modulo.objects.filter(curso=self.instance.modulo.curso)
            self.fields['curso'].initial = self.instance.modulo.curso
        elif 'curso' in self.data:
            try:
                curso_id = int(self.data.get('curso'))
                self.fields['modulo'].queryset = Modulo.objects.filter(curso_id=curso_id)
            except (ValueError, TypeError):
                self.fields['modulo'].queryset = Modulo.objects.none()
