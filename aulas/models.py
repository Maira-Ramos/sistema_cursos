
from django.db import models
from cursos.models import Modulo

class Aula(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='aulas')
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    link_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
