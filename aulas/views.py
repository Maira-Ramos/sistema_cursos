# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aula
from .forms import AulaForm

# LISTAGEM
def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aulas/lista.html', {'aulas': aulas})


# DETALHES
def detalhes_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    return render(request, 'aulas/detalhes.html', {'aula': aula})

# CRIAÇÃO
def criar_aula(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aulas:lista')
    else:
        form = AulaForm()
    return render(request, 'aulas/form.html', {'form': form})

# EDIÇÃO
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

# EXCLUSÃO
def excluir_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    if request.method == 'POST':
        aula.delete()
        return redirect('aulas:lista')
    return render(request, 'aulas/excluir.html', {'aula': aula})
