from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coffeshop.accounts'

    def ready(self):
        import coffeshop.accounts.signals
        result = super().ready()
        return result


