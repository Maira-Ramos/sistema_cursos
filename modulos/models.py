from django.db import models
from cursos.models import Curso

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"

        