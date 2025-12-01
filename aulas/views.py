from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Aula
from .forms import AulaForm

# LISTAGEM → qualquer usuário logado
@login_required
def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/lista.html', {'aulas': aulas})


# DETALHES → qualquer usuário logado
@login_required
def detalhes_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    return render(request, 'aulas/detalhes.html', {'aula': aula})


# CRIAÇÃO → apenas professores
@login_required
@permission_required("aulas.add_aula", raise_exception=True)
def criar_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aulas:lista')
    else:
        form = AulaForm()
    return render(request, 'aulas/form.html', {'form': form})


# EDIÇÃO → apenas professores
@login_required
@permission_required("aulas.change_aula", raise_exception=True)
def editar_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('aulas:lista')
    else:
        form = AulaForm(instance=aula)
    return render(request, 'aulas/form.html', {'form': form})


# EXCLUSÃO → apenas professores
@login_required
@permission_required("aulas.delete_aula", raise_exception=True)
def excluir_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == 'POST':
        aula.delete()
        return redirect('aulas:lista')
    return render(request, 'aulas/excluir.html', {'aula': aula})
