from django.shortcuts import render

def home(request):
    context = {}
    
    # Verifica se o usuário está autenticado para poder checar os grupos
    if request.user.is_authenticated:
        
        
        is_professor = request.user.groups.filter(name='Professor').exists()
        
        is_aluno = request.user.groups.filter(name='Aluno').exists()
        
        context['is_professor'] = is_professor
        context['is_aluno'] = is_aluno
    
    return render(request, 'home.html', context)