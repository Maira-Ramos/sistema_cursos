from django.urls import path
from . import views

app_name = 'inscricoes'

urlpatterns = [
    path('criar/', views.criar_inscricao, name='criar'),
]
