from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
]
