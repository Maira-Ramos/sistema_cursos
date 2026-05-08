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
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    
    
    path("api/", include("cursos.api_urls")),
    path("api/", include("alunos.api_urls")),
    path("api/", include("aulas.api_urls")),
    path("api/", include("modulos.api_urls")),
    path("api/", include('inscricoes.api_urls')),
    path("api/", include("usuarios.api_urls")),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
