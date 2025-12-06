from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from .models import Modulo
from .forms import ModuloForm

# LISTAR MÓDULOS → qualquer usuário logado
@login_required
def listar_modulos(request):
    modulos = Modulo.objects.select_related("curso").all()
    user = request.user

    try:
        grupo_professor = Group.objects.get(name="Professor")
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        is_professor = False

    return render(request, "modulos/lista_modulos.html", {
        "modulos": modulos,
        "is_professor": is_professor,
    })

# DETALHE MÓDULO → qualquer usuário logado
@login_required
def detalhe_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    return render(request, "modulos/detalhe_modulo.html", {"modulo": modulo})

# CRIAR MÓDULO → apenas professores
@login_required
def criar_modulo(request):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    if request.method == "POST":
        form = ModuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_modulos")
    else:
        form = ModuloForm()

    return render(request, "modulos/form_modulo.html", {"form": form})

# EDITAR MÓDULO → apenas professores
@login_required
def editar_modulo(request, id):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    modulo = get_object_or_404(Modulo, id=id)

    if request.method == "POST":
        form = ModuloForm(request.POST, instance=modulo)
        if form.is_valid():
            form.save()
            return redirect("listar_modulos")
    else:
        form = ModuloForm(instance=modulo)

    return render(request, "modulos/form_modulo.html", {"form": form, "modulo": modulo})

# EXCLUIR MÓDULO → apenas professores
@login_required
def excluir_modulo(request, id):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    modulo = get_object_or_404(Modulo, id=id)

    if request.method == "POST":
        modulo.delete()
        return redirect("listar_modulos")

    return render(request, "modulos/confirmar_exclusao.html", {"modulo": modulo})
