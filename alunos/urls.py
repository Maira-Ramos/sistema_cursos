from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.listar_alunos, name='listar'),
    path('novo/', views.cadastrar_aluno, name='cadastrar'),
    path('<int:id>/', views.detalhes_aluno, name='detalhes'),
    path('<int:id>/editar/', views.editar_aluno, name='editar'),
    path('<int:id>/excluir/', views.excluir_aluno, name='excluir'),
  

]
