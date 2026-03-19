from django.apps import AppConfig


class BankaccountConfig(AppConfig):
    name = 'bankaccount'


    def ready(self):
        import bankaccount.signals
            