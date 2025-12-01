from django.db import models
from cursos.models import Curso

class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=1)

    class Meta:
        permissions = [
            ("ver_modulo", "Pode visualizar módulos"),
            ("criar_modulo", "Pode criar módulos"),
            ("editar_modulo", "Pode editar módulos"),
            ("deletar_modulo", "Pode deletar módulos"),
        ]

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"
