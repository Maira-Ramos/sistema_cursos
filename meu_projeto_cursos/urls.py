from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('cursos/', include('cursos.urls')),
    path('modulos/', include('modulos.urls')),
    path('alunos/', include('alunos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('aulas/', include('aulas.urls')),
    path('inscricoes/', include('inscricoes.urls')),

]
