from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_modulos, name="listar_modulos"),
    path("criar/", views.criar_modulo, name="criar_modulo"),
    path("editar/<int:id>/", views.editar_modulo, name="editar_modulo"),
    path("excluir/<int:id>/", views.excluir_modulo, name="excluir_modulo"),
]
