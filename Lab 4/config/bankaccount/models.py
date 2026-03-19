from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models import Q, CheckConstraint, Index
from django.forms import ValidationError

from .utils import Helper

# Create your models here.
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=15, unique=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add= True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'bank_accounts'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(balance__gte=0.00),
                name='balance_gt_zero'
            )
        ]
        indexes = [
            models.Index(fields=['balance'])
        ]
    def __str__(self):
        return f'{self.user.username} - {self.account_number}'
    
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = Helper.generate_account_number(prefix='EG')
        super().save(*args, **kwargs)




class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'DP', 'Deposit'
        WITHDRAWAL = 'WD', 'Withdrawal'

    transaction_number = models.CharField(max_length=12, unique=True, blank=True)
    transaction_type = models.CharField(max_length=2, choices=TransactionType.choices)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.account.account_number} - {self.amount}'
    
    def clean(self):
        if self.transaction_type == self.TransactionType.WITHDRAWAL and self.amount > self.account.balance:
            raise ValidationError('Balance not enough for withdrawal.')
        super().clean()
    
    def save(self, *args, **kwargs):
        if not self.transaction_number:
            self.transaction_number = Helper.generate_transaction_number()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'transactions'
        ordering = ['-created_at']
