from django.apps import AppConfig


class SamsConfig(AppConfig):
    name = 'SAMS'

    def ready(self):
        import SAMS.encodingModel