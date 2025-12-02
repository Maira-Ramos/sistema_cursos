from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("usuarios.urls")),      # raiz vai para login/home do app usuarios
    path("cursos/", include("cursos.urls")),
    path("modulos/", include("modulos.urls")),
    path("alunos/", include("alunos.urls")),
    path("aulas/", include("aulas.urls")),
    path("inscricoes/", include("inscricoes.urls")),
]
