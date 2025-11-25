from django.urls import path
from . import views

app_name = 'aulas'

urlpatterns = [
    path('', views.lista_aulas, name='lista'),
    path('nova/', views.criar_aula, name='criar'),
    path('<int:id>/', views.detalhes_aula, name='detalhes'),
    path('<int:id>/editar/', views.editar_aula, name='editar'),
    path('<int:id>/excluir/', views.excluir_aula, name='excluir'),
]
