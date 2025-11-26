from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import FormAluno
from cursos.models import Curso  # ajustar se o nome for outro


# 1) Listagem
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})


# 2) Detalhes
def detalhes_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    cursos_inscritos = Curso.objects.filter(inscricoes__aluno=aluno)

    return render(request, 'alunos/detalhes.html', {
        'aluno': aluno,
        'cursos_inscritos': cursos_inscritos,
    })


# 3) Cadastro
def cadastrar_aluno(request):
    formulario = FormAluno(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('alunos:listar')

    return render(request, 'alunos/form.html', {'form': formulario})


# 4) Edição
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    formulario = FormAluno(request.POST or None, instance=aluno)

    if formulario.is_valid():
        formulario.save()
        return redirect('alunos:listar')

    return render(request, 'alunos/form.html', {'form': formulario})


# 5) Exclusão
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == "POST":
        aluno.delete()  # já remove inscrições por causa do CASCADE
        return redirect('alunos:listar')

    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})



