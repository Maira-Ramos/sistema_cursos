from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Inscricao
from .forms import InscricaoForm

def listar_inscricoes(request):
    inscricoes = Inscricao.objects.all()
    return render(request, "inscricoes/lista.html", {"inscricoes": inscricoes})


# DETALHES
def detalhes_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    total = Inscricao.objects.filter(aluno=inscricao.aluno).count()

    return render(request, "inscricoes/detalhes.html", {
        "inscricao": inscricao,
        "total": total
    })


# CRIAR
def criar_inscricao(request):
    if request.method == "POST":
        form = InscricaoForm(request.POST)

        if form.is_valid():
            aluno = form.cleaned_data["aluno"]
            curso = form.cleaned_data["curso"]
            if Inscricao.objects.filter(aluno=aluno, curso=curso).exists():
                messages.error(request, "Este aluno já está inscrito neste curso.")
                return redirect("inscricoes:criar")

            form.save()
            messages.success(request, "Inscrição criada com sucesso!")
            return redirect("inscricoes:listar")
    else:
        form = InscricaoForm()

    return render(request, "inscricoes/criar.html", {"form": form})

from django.urls import path
from . import views

app_name = 'inscricoes'

urlpatterns = [
    path('criar/', views.criar_inscricao, name='criar'),
]

# EXCLUIR
def excluir_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)

    if request.method == "POST":
        inscricao.delete()
        messages.success(request, "Inscrição removida com sucesso!")
        return redirect("inscricoes:listar")

    return render(request, "inscricoes/excluir.html", {"inscricao": inscricao})