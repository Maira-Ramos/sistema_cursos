from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from .models import Curso
from .forms import CursoForm

# LISTAR CURSOS → qualquer usuário logado
@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    user = request.user

    try:
        grupo_professor = Group.objects.get(name="Professor")
        is_professor = grupo_professor in user.groups.all()
    except Group.DoesNotExist:
        is_professor = False

    return render(request, 'cursos/lista.html', {
        'cursos': cursos,
        'is_professor': is_professor
    })


# DETALHE CURSO → qualquer usuário logado
@login_required
def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    try:
        grupo_professor = Group.objects.get(name="Professor")
        is_professor = grupo_professor in request.user.groups.all()
    except Group.DoesNotExist:
        is_professor = False

    return render(request, 'cursos/detalhe.html', {
        'curso': curso,
        'is_professor': is_professor
    })


# CRIAR CURSO → apenas professores
@login_required
def criar_curso(request):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()

    return render(request, 'cursos/form.html', {
        'form': form,
        'titulo': 'Criar Curso'
    })


# EDITAR CURSO → apenas professores
@login_required
def editar_curso(request, id):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'cursos/form.html', {
        'form': form,
        'titulo': 'Editar Curso'
    })


# EXCLUIR CURSO → apenas professores
@login_required
def excluir_curso(request, id):
    try:
        grupo_professor = Group.objects.get(name="Professor")
        if grupo_professor not in request.user.groups.all():
            raise PermissionDenied
    except Group.DoesNotExist:
        raise PermissionDenied

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')

    return render(request, 'cursos/confirmar_excluir.html', {'curso': curso})
