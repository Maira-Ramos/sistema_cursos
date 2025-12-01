from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group  # <--- IMPORT ADICIONADO
from .models import Curso
from .forms import CursoForm

# LISTAGEM → qualquer usuário logado
@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    user = request.user # Obter o usuário logado

    # LÓGICA ADICIONADA: Verificar se o usuário é professor
    try:
        # Tenta obter o grupo 'Professor'
        grupo_professor = Group.objects.get(name="Professor") 
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        # Fallback seguro
        is_professor = False 

    context = {
        'cursos': cursos,
        "is_professor": is_professor, # <--- VARIÁVEL ADICIONADA AO CONTEXTO
    }
    
    return render(request, 'cursos/lista.html', context)


# DETALHES → qualquer usuário logado
@login_required
def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})


# CRIAÇÃO → apenas professores
@login_required
@permission_required("cursos.add_curso", raise_exception=True)
def criar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/form.html', {'form': form, 'titulo': 'Criar Curso'})


# EDIÇÃO → apenas professores
@login_required
@permission_required("cursos.change_curso", raise_exception=True)
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/form.html', {'form': form, 'titulo': 'Editar Curso'})


# EXCLUSÃO → apenas professores
@login_required
@permission_required("cursos.delete_curso", raise_exception=True)
def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:listar_cursos')
    return render(request, 'cursos/confirmar_excluir.html', {'curso': curso})