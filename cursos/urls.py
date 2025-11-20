from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('criar/', views.criar_curso, name='criar_curso'),
    path('<int:id>/', views.detalhe_curso, name='detalhe_curso'),
    path('<int:id>/editar/', views.editar_curso, name='editar_curso'),
    path('<int:id>/excluir/', views.excluir_curso, name='excluir_curso'),
]
