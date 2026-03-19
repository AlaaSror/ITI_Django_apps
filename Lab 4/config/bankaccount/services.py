from .models import BankAccount, Transaction


class ManageBankAccount:
    @staticmethod
    def get_account_by_pk(self, pk):
        try:
            return BankAccount.objects.get(pk=pk)
        except BankAccount.DoesNotExist:
            return None
        
    @staticmethod
    def create_bank_account(self, user):
        return BankAccount.objects.create(user=user)
    
    @staticmethod
    def get_all_bank_accounts(self):
        return BankAccount.objects.all()