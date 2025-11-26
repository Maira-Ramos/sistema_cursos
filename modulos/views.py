from django.shortcuts import render, redirect, get_object_or_404
from .models import Modulo
from .forms import ModuloForm

def listar_modulos(request):
    modulos = Modulo.objects.select_related("curso").all()
    return render(request, "modulos/lista_modulos.html", {"modulos": modulos})

def detalhe_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    return render(request, "modulos/detalhe_modulo.html", {"modulo": modulo})

def criar_modulo(request):
    form = ModuloForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_modulos")
    return render(request, "modulos/form_modulo.html", {"form": form})

def editar_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)
    form = ModuloForm(request.POST or None, instance=modulo)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_modulos")
    return render(request, "modulos/form_modulo.html", {"form": form, "modulo": modulo})

def excluir_modulo(request, id):
    modulo = get_object_or_404(Modulo, id=id)

    if request.method == "POST":
        modulo.delete()
        return redirect("listar_modulos")

    # página de confirmação
    return render(request, "modulos/confirmar_exclusao.html", {"modulo": modulo})
