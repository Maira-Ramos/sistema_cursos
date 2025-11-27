from django.urls import path
from . import views

app_name = "inscricoes"

urlpatterns = [
    path("", views.listar_inscricoes, name="listar"),
    path("criar/", views.criar_inscricao, name="criar"),
    path("<int:id>/", views.detalhes_inscricao, name="detalhes"),
    path("<int:id>/excluir/", views.excluir_inscricao, name="excluir"),
]
