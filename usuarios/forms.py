from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import PermissaoCustom

CODIGO_PROFESSOR = "PROF123"

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label="Nome completo",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    codigo_professor = forms.CharField(
        max_length=50,
        required=False,
        label="Código do professor (se aplicável)",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'is_active', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        # Salvar nome completo no first_name só para ter algo
        user.first_name = self.cleaned_data['nome_completo']

        if commit:
            user.save()

            codigo = self.cleaned_data.get("codigo_professor")

            # Define o grupo correto
            if codigo == CODIGO_PROFESSOR:
                grupo = Group.objects.get(name="Professor")
            else:
                grupo = Group.objects.get(name="Aluno")

            user.groups.add(grupo)

        return user
class UserEditForm(forms.ModelForm):
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label="Nome completo",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Preencher o campo 'nome_completo' com o que você salvou no first_name
        if self.instance:
            self.fields['nome_completo'].initial = self.instance.first_name

    def save(self, commit=True):
        user = super().save(commit=False)

        # Salva o nome completo no first_name novamente
        user.first_name = self.cleaned_data['nome_completo']

        if commit:
            user.save()
        return user
