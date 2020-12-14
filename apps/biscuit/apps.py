from django.apps import AppConfig


class BiscuitConfig(AppConfig):
    name = 'apps.biscuit'
    label = 'apps_biscuit'

    def ready(self):
        import apps.biscuit.signals.biscuit
