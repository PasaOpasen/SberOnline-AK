from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    verbose = 'api'

    def ready(self):
        pass
