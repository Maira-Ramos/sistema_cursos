from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Aluno
from .forms import FormAluno
from cursos.models import Curso


def usuario_e_professor(user):
    """Retorna True se o usuário pertence ao grupo Professor."""
    try:
        grupo_professor = Group.objects.get(name="Professor")
        return grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        return False


# 1) Listar alunos → APENAS professor
@login_required
def listar_alunos(request):
    if not usuario_e_professor(request.user):
        return redirect('/')  # impede Forbidden
    
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
        'is_professor': True
    }
    return render(request, 'alunos/lista.html', context)


# 2) Detalhes → QUALQUER usuário logado
@login_required
def detalhes_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    cursos_inscritos = Curso.objects.filter(inscricoes__aluno=aluno)

    context = {
        'aluno': aluno,
        'cursos_inscritos': cursos_inscritos,
        'is_professor': usuario_e_professor(request.user)
    }

    return render(request, 'alunos/detalhe.html', context)


# 3) Cadastro → APENAS professor
@login_required
def cadastrar_aluno(request):
    if not usuario_e_professor(request.user):
        return redirect('/')

    form = FormAluno(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('alunos:listar')

    return render(request, 'alunos/form.html', {
        'form': form,
        'is_professor': True
    })


# 4) Editar → APENAS professor
@login_required
def editar_aluno(request, id):
    if not usuario_e_professor(request.user):
        return redirect('/')

    aluno = get_object_or_404(Aluno, id=id)
    form = FormAluno(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('alunos:listar')

    return render(request, 'alunos/form.html', {
        'form': form,
        'is_professor': True
    })


# 5) Excluir → APENAS professor
@login_required
def excluir_aluno(request, id):
    if not usuario_e_professor(request.user):
        return redirect('/')

    aluno = get_object_or_404(Aluno, id=id)

    if request.method == "POST":
        aluno.delete()
        return redirect('alunos:listar')

    return render(request, 'alunos/excluir.html', {
        'aluno': aluno,
        'is_professor': True
    })
