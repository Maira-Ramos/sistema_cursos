from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        permissions = [
            ("ver_curso", "Pode visualizar cursos"),
            ("criar_curso", "Pode criar cursos"),
            ("editar_curso", "Pode editar cursos"),
            ("deletar_curso", "Pode deletar cursos"),
        ]
