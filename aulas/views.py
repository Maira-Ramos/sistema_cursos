from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Aula
from .forms import AulaForm
from cursos.models import Curso
from modulos.models import Modulo 
from django.http import JsonResponse


# LISTAGEM → qualquer usuário logado

@login_required
def lista_aulas(request):
    aulas = Aula.objects.all()
    context = {
        'aulas': aulas,
        'can_criar': request.user.has_perm('aulas.add_aula'),
        'is_professor': request.user.groups.filter(name='Professores').exists(),
    }
    return render(request, 'aulas/lista.html', context)



# DETALHES → qualquer usuário logado
@login_required
def detalhes_aula(request, id):
    aula = get_object_or_404(Aula, id=id)
    return render(request, 'aulas/detalhes.html', {'aula': aula})




@login_required
def criar_aula(request):
    form = AulaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('aulas:lista')

    context = {
        'form': form,
        'is_professor': request.user.groups.filter(name='Professores').exists(),
    }
    return render(request, 'aulas/form.html', context)





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

def ajax_load_modulos(request):
    curso_id = request.GET.get('curso_id')
    modulos = Modulo.objects.filter(curso_id=curso_id).order_by('ordem')
    data = [{"id": m.id, "nome": m.nome} for m in modulos]
    return JsonResponse(data, safe=False)
