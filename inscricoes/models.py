
from django.db import models
from alunos.models import Aluno
from cursos.models import Curso

class Inscricao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('aluno', 'curso')  # evita inscrição duplicada

    def __str__(self):
        return f"{self.aluno.nome} → {self.curso.nome}"


