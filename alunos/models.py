from django.db import models
from cursos.models import Curso  

class Aluno(models.Model):
    nome = models.CharField("Nome completo", max_length=200)
    email = models.EmailField("E-mail", unique=True)
    data_nascimento = models.DateField("Data de nascimento")

    def __str__(self):
        return self.nome

    class Meta:
        permissions = [
            ("ver_aluno", "Pode visualizar alunos"),
            ("criar_aluno", "Pode criar alunos"),
            ("editar_aluno", "Pode editar alunos"),
            ("deletar_aluno", "Pode deletar alunos"),
        ]
