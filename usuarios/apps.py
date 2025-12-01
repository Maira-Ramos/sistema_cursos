from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        # Import aqui dentro → só será executado depois que as apps estiverem carregadas
        from django.contrib.auth.models import Group

        grupos_necessarios = ["Aluno", "Professor"]

        for nome in grupos_necessarios:
            Group.objects.get_or_create(name=nome)
