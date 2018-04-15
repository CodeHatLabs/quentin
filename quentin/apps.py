from django.apps import AppConfig


class QuentinConfig(AppConfig):

    name = 'quentin'

    def ready(self):
        from django.conf import settings
        from ebpy import conf
        conf.settings = settings


