from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group  # <--- IMPORT ADICIONADO
from .models import Modulo
from .forms import ModuloForm

# LISTAGEM → qualquer usuário logado
@login_required
def listar_modulos(request):
    modulos = Modulo.objects.select_related("curso").all()
    user = request.user  # Obtendo o usuário logado

    # LÓGICA DE VERIFICAÇÃO DE GRUPO ADICIONADA
    try:
        # Tenta obter o grupo 'Professor'
        grupo_professor = Group.objects.get(name="Professor")
        # Verifica se o usuário pertence a este grupo
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        # Fallback seguro
        is_professor = False

    context = {
        "modulos": modulos,
        "is_professor": is_professor,  # <--- VARIÁVEL ENVIADA AO TEMPLATE
    }
    
    return render(request, "modulos/lista_modulos.html", context)


# DETALHES → qualquer usuário logado
@login_required
def detalhe_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    return render(request, "modulos/detalhe_modulo.html", {"modulo": modulo})


# CRIAR → apenas professores
@login_required
@permission_required("modulos.add_modulo", raise_exception=True)
def criar_modulo(request):
    form = ModuloForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("modulos:listar_modulos")
    return render(request, "modulos/form_modulo.html", {"form": form})


# EDIÇÃO → apenas professores
@login_required
@permission_required("modulos.change_modulo", raise_exception=True)
def editar_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    form = ModuloForm(request.POST or None, instance=modulo)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("modulos:listar_modulos")
    return render(request, "modulos/form_modulo.html", {"form": form, "modulo": modulo})


# EXCLUSÃO → apenas professores
@login_required
@permission_required("modulos.delete_modulo", raise_exception=True)
def excluir_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)

    if request.method == "POST":
        modulo.delete()
        return redirect("modulos:listar_modulos")

    return render(request, "modulos/confirmar_exclusao.html", {"modulo": modulo})