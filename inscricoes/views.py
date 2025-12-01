from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Inscricao
from .forms import InscricaoForm

# LISTAGEM → qualquer usuário logado
@login_required
def listar_inscricoes(request):
    inscricoes = Inscricao.objects.all()
    return render(request, "inscricoes/lista.html", {"inscricoes": inscricoes})


# DETALHES → qualquer usuário logado
@login_required
def detalhes_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    total = Inscricao.objects.filter(aluno=inscricao.aluno).count()

    return render(request, "inscricoes/detalhes.html", {
        "inscricao": inscricao,
        "total": total
    })


# CRIAR → apenas professores
@login_required
@permission_required("inscricoes.add_inscricao", raise_exception=True)
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

    return render(request, "inscricoes/form.html", {"form": form})


# EXCLUIR → apenas professores
@login_required
@permission_required("inscricoes.delete_inscricao", raise_exception=True)
def excluir_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)

    if request.method == "POST":
        inscricao.delete()
        messages.success(request, "Inscrição removida com sucesso!")
        return redirect("inscricoes:listar")

    return render(request, "inscricoes/excluir.html", {"inscricao": inscricao})
