from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('', views.home, name='home'),           # home/dashboard
    path('login/', views.login_user, name='login'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('logout/', views.logout_user, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
]