from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Aluno

# ---------------------------------------------------
# 1️⃣ Criar ou sincronizar Aluno quando User é criado ou atualizado
# ---------------------------------------------------
@receiver(post_save, sender=User)
def criar_ou_sincronizar_aluno(sender, instance, created, **kwargs):
    """
    Cria ou sincroniza o registro Aluno sempre que o User for criado
    ou atualizado, garantindo que usuários já existentes também sejam considerados.
    """
    try:
        grupo_aluno = Group.objects.get(name="Aluno")
    except Group.DoesNotExist:
        return

    # Verifica se usuário está no grupo Aluno
    if grupo_aluno in instance.groups.all():
        aluno, novo = Aluno.objects.get_or_create(
            user=instance,
            defaults={
                "nome": instance.get_full_name() or instance.username,
                "email": instance.email,
                "data_nascimento": "2000-01-01",  # padrão
            }
        )

        # Sincroniza nome e email se já existia
        alterado = False
        novo_nome = instance.get_full_name() or instance.username
        if aluno.nome != novo_nome:
            aluno.nome = novo_nome
            alterado = True
        if aluno.email != instance.email:
            aluno.email = instance.email
            alterado = True
        if alterado:
            aluno.save()


# ---------------------------------------------------
# 2️⃣ Criar Aluno se usuário é adicionado ao grupo
# ---------------------------------------------------
@receiver(m2m_changed, sender=User.groups.through)
def criar_aluno_quando_entra_no_grupo(sender, instance, action, pk_set, **kwargs):
    """
    Garante criação de Aluno caso usuário existente seja adicionado ao grupo "Aluno"
    """
    if action != "post_add":
        return

    try:
        grupo_aluno = Group.objects.get(name="Aluno")
    except Group.DoesNotExist:
        return

    if grupo_aluno.id in pk_set:
        # Evita duplicação
        if not Aluno.objects.filter(user=instance).exists():
            Aluno.objects.create(
                user=instance,
                nome=instance.get_full_name() or instance.username,
                email=instance.email,
                data_nascimento="2000-01-01"
            )
