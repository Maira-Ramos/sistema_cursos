from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from .models import Modulo
from .forms import ModuloForm

# LISTAGEM → qualquer usuário logado
@login_required
def listar_modulos(request):
    modulos = Modulo.objects.select_related("curso").all()
    user = request.user  # Obtendo o usuário logado

    # LÓGICA DE VERIFICAÇÃO DE GRUPO ADICIONADA
    try:
        grupo_professor = Group.objects.get(name="Professor")
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        is_professor = False

    context = {
        "modulos": modulos,
        "is_professor": is_professor,
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
        return redirect("listar_modulos")  # <<< CORRIGIDO
    return render(request, "modulos/form_modulo.html", {"form": form})


# EDIÇÃO → apenas professores
@login_required
@permission_required("modulos.change_modulo", raise_exception=True)
def editar_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    form = ModuloForm(request.POST or None, instance=modulo)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_modulos")  # <<< CORRIGIDO
    return render(request, "modulos/form_modulo.html", {"form": form, "modulo": modulo})


# EXCLUSÃO → apenas professores
@login_required
@permission_required("modulos.delete_modulo", raise_exception=True)
def excluir_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)

    if request.method == "POST":
        modulo.delete()
        return redirect("listar_modulos")  # já estava correto

    return render(request, "modulos/confirmar_exclusao.html", {"modulo": modulo})
