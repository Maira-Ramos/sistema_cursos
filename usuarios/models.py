from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

class PermissaoCustom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pode_criar_curso = models.BooleanField(default=False)
    pode_editar_aluno = models.BooleanField(default=False)
    pode_deletar_postagem = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("criar_curso", "Pode criar curso"),
            ("editar_aluno", "Pode editar aluno"),
            ("deletar_postagem", "Pode deletar postagem"),
        ]

    def __str__(self):
        return f"Permissões de {self.user.username}"


@receiver(post_save, sender=PermissaoCustom)
def sincronizar_permissoes(sender, instance, **kwargs):
    user = instance.user

    # Limpa permissões antigas
    user.user_permissions.clear()

    mapping = {
        'pode_criar_curso': 'criar_curso',
        'pode_editar_aluno': 'editar_aluno',
        'pode_deletar_postagem': 'deletar_postagem',
    }

    for campo, codename in mapping.items():
        if getattr(instance, campo):
            try:
                perm = Permission.objects.get(codename=codename)
                user.user_permissions.add(perm)
            except Permission.DoesNotExist:
                pass
