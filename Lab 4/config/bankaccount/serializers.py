from rest_framework import serializers
from .models import BankAccount, Transaction
from .services import ManageBankAccount

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        read_only_fields = ['account_number','balance', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        user = validated_data.get('user')
        return ManageBankAccount.create_bank_account(self, user)

