from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'apps.product'
    label = 'apps_product'

    def ready(self):
        import apps.product.signals.product


