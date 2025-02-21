from django.apps import AppConfig

class SamethreadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "samethread"

    def ready(self):
        import samethread.signals  # Ensure signals are loaded