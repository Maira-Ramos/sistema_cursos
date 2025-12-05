from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from alunos.views import usuario_e_professor
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
def criar_inscricao(request):
    # SE FOR ALUNO → restringe o formulário
    if hasattr(request.user, "aluno"):
        aluno_logado = request.user.aluno
        aluno_selecionado = aluno_logado
    else:
        # Se for professor, pode escolher aluno livremente
        aluno_selecionado = None

    if request.method == "POST":
        form = InscricaoForm(request.POST)

        if form.is_valid():
            curso = form.cleaned_data["curso"]

            # Para alunos → travar aluno no logado
            if aluno_selecionado:
                aluno = aluno_selecionado
            else:
                aluno = form.cleaned_data["aluno"]

            # evitar duplicidade
            if Inscricao.objects.filter(aluno=aluno, curso=curso).exists():
                messages.error(request, "Este aluno já está inscrito neste curso.")
                return redirect("inscricoes:criar")

            inscricao = form.save(commit=False)
            inscricao.aluno = aluno
            inscricao.save()

            messages.success(request, "Inscrição criada com sucesso!")
            return redirect("inscricoes:listar")

    else:
        form = InscricaoForm()

    return render(request, "inscricoes/form.html", {"form": form, "aluno_selecionado": aluno_selecionado})


# 4) Editar → APENAS professor
@login_required
def editar_inscricao(request, id):
    if not usuario_e_professor(request.user):
        return redirect('/')

    inscricao = get_object_or_404(Inscricao, id=id)
    form = InscricaoForm(request.POST or None, instance=inscricao)

    if form.is_valid():
        form.save()
        return redirect('inscricoes:listar')
  
    return render(request, 'inscricoes/form.html', {
        'form': form,
        'is_professor': True

    })


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
