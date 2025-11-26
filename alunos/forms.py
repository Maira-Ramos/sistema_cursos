from django import forms
from .models import Aluno

class FormAluno(forms.ModelForm):
    data_nascimento = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento']

