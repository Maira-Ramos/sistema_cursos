from django.apps import AppConfig

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        # Apenas importa os signals — NÃO executa lógica de banco aqui
        import usuarios.signals
