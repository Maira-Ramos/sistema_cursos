from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inscricao
from .forms import InscricaoForm

def criar_inscricao(request):
    if request.method == "POST":
        form = InscricaoForm(request.POST)

        if form.is_valid():
            aluno = form.cleaned_data['aluno']
            curso = form.cleaned_data['curso']

            # impede duplicidade
            if Inscricao.objects.filter(aluno=aluno, curso=curso).exists():
                messages.error(request, "Este aluno já está inscrito neste curso.")
                return redirect('inscricoes:criar')

            form.save()
            messages.success(request, "Inscrição cadastrada com sucesso!")
            return redirect('inscricoes:listar')

    else:
        form = InscricaoForm()

    return render(request, 'inscricoes/criar_inscricao.html', {'form': form})
