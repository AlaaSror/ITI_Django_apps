from django.apps import apps
import random
import string

class Helper:

    @staticmethod
    def generate_account_number(prefix=None):
        model = apps.get_model('bankaccount', 'BankAccount')
        while True:
            account_number_unique = ''.join(random.choices(string.digits, k=12))
            if prefix:
                account_number = f'{prefix}{account_number_unique}'
            if not model.objects.filter(account_number=account_number_unique).exists():
                return account_number

    @staticmethod
    def generate_transaction_number():
        model = apps.get_model('bankaccount', 'Transaction')
        while True:
            transaction_number_unique = ''.join(random.choices(string.digits, k=12))
            if not model.objects.filter(transaction_number=transaction_number_unique).exists():
                return transaction_number_unique