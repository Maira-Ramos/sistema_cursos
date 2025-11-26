from django.db import models
from cursos.models import Curso  # Ajuste se o nome da app de cursos for outro

class Aluno(models.Model):
    nome = models.CharField("Nome completo", max_length=200)
    email = models.EmailField("E-mail", unique=True)
    data_nascimento = models.DateField("Data de nascimento")

    def __str__(self):
        return self.nome



