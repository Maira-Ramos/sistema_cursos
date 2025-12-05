from django.db import models
from modulos.models import Modulo
  # importa o modelo Modulo

class Aula(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='aulas')
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    link_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = [
            ("ver_aula", "Pode visualizar aulas"),
            ("criar_aula", "Pode criar aulas"),
            ("editar_aula", "Pode editar aulas"),
            ("deletar_aula", "Pode deletar aulas"),
        ]
