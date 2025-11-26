from django.db import models
from django.contrib.auth.models import User

class PermissaoCustom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pode_criar_curso = models.BooleanField(default=False)
    pode_editar_aluno = models.BooleanField(default=False)
    pode_deletar_postagem = models.BooleanField(default=False)

    def __str__(self):
        return f'Permissões de {self.user.username}'
