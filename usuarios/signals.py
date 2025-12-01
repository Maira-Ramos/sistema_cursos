from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def criar_grupos(sender, **kwargs):

    grupos = {
        'professor': [
            'add_curso', 'change_curso', 'delete_curso',
            'add_modulo', 'change_modulo', 'delete_modulo',
            'add_aula', 'change_aula', 'delete_aula',
        ],
        'aluno': [
            # aluno não possui permissões de criação/edição
        ]
    }

    for nome_grupo, permissoes in grupos.items():
        grupo, _ = Group.objects.get_or_create(name=nome_grupo)

        # aplicar as permissões às quais o grupo tem direito
        for codename in permissoes:
            try:
                perm = Permission.objects.get(codename=codename)
                grupo.permissions.add(perm)
            except Permission.DoesNotExist:
                pass
