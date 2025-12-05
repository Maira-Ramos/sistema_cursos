from django.db import models
from django.contrib.auth.models import User
from cursos.models import Curso  

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
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
