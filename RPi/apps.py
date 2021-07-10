from django.apps import AppConfig


class RpiConfig(AppConfig):
    name = 'RPi'

    def ready(self):
        import RPi.matchingModel
