from django import forms
from modulos.models import Modulo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PermissaoCustom

# Form de criação de usuário com nome completo
class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label="Nome completo",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

# Form de alteração de usuário com nome completo
class CustomUserChangeForm(UserChangeForm):
    nome_completo = forms.CharField(
        max_length=150,
        required=True,
        label="Nome completo",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(),
        }

# Form de permissões customizadas
class PermissaoForm(forms.ModelForm):
    class Meta:
        model = PermissaoCustom
        fields = ['pode_criar_curso', 'pode_editar_aluno', 'pode_deletar_postagem']
        widgets = {
            'pode_criar_curso': forms.CheckboxInput(),
            'pode_editar_aluno': forms.CheckboxInput(),
            'pode_deletar_postagem': forms.CheckboxInput(),
        }
