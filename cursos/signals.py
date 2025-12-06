from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command

@receiver(post_migrate)
def carregar_dados_iniciais(sender, **kwargs):
    """
    Carrega o fixture de dados iniciais automaticamente
    após as migrações do app 'cursos'.
    """
    from django.apps import apps
    if sender.name == 'cursos':
        try:
            call_command('loaddata', 'dados_iniciais.json', verbosity=0)
            print("✅ Dados iniciais carregados com sucesso!")
        except Exception as e:
            print(f"⚠️ Erro ao carregar dados iniciais: {e}")
