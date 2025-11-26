# usuarios/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm, PermissaoForm
from .models import PermissaoCustom
from modulos.models import Modulo

# Decorator para administradores
def administrador_required(view_func):
    return user_passes_test(
        lambda u: u.is_authenticated and u.groups.filter(name='Administrador').exists()
    )(view_func)

# Listar todos os usuários
#@login_required
#@administrador_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Criar novo usuário
#@login_required
#@administrador_required
def criar_usuario(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        perm_form = PermissaoForm(request.POST)
        if user_form.is_valid() and perm_form.is_valid():
            # Salva usuário
            user = user_form.save(commit=False)
            # Campo 'nome_completo' (do form) usado para popular first_name e last_name
            nome_completo = user_form.cleaned_data.get('nome_completo', '')
            if nome_completo:
                partes = nome_completo.split()
                user.first_name = partes[0]
                user.last_name = ' '.join(partes[1:]) if len(partes) > 1 else ''
            user.save()
            # Salva permissões
            perm = perm_form.save(commit=False)
            perm.user = user
            perm.save()
            return redirect('lista_usuarios')
    else:
        user_form = CustomUserCreationForm()
        perm_form = PermissaoForm()
    return render(request, 'usuarios/form.html', {'user_form': user_form, 'perm_form': perm_form})

# Editar usuário
#@login_required
#@administrador_required
def editar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    perm, created = PermissaoCustom.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        perm_form = PermissaoForm(request.POST, instance=perm)
        if user_form.is_valid() and perm_form.is_valid():
            user = user_form.save(commit=False)
            nome_completo = user_form.cleaned_data.get('nome_completo', '')
            if nome_completo:
                partes = nome_completo.split()
                user.first_name = partes[0]
                user.last_name = ' '.join(partes[1:]) if len(partes) > 1 else ''
            user.save()
            perm_form.save()
            return redirect('lista_usuarios')
    else:
        initial_data = {'nome_completo': f"{user.first_name} {user.last_name}"}
        user_form = CustomUserChangeForm(instance=user, initial=initial_data)
        perm_form = PermissaoForm(instance=perm)

    return render(request, 'usuarios/form.html', {'user_form': user_form, 'perm_form': perm_form})

# Deletar usuário
#@login_required
#@administrador_required
def deletar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/confirm_delete.html', {'usuario': user})
