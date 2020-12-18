from django.apps import AppConfig


class WarehouseConfig(AppConfig):
    name = 'apps.warehouse'
    label = 'apps_warehouse'

    def ready(self):
        import apps.warehouse.signals.income

