from django.urls import path
from . import views

app_name = "inscricoes"

urlpatterns = [
    path("", views.listar_inscricoes, name="listar"),
    path("form/", views.criar_inscricao, name="form"),
    path("<int:id>/", views.detalhes_inscricao, name="detalhes"),
    path('<int:id>/editar/', views.editar_inscricao, name='editar'),
    path("<int:id>/excluir/", views.excluir_inscricao, name="excluir"),
    path('api/inscricoes/', views.lista_inscricoes_api, name='api_inscricoes'),
]   


