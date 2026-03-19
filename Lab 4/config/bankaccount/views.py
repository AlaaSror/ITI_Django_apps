from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BankAccount, Transaction
from .serializers import BankAccountSerializer
from .services import ManageBankAccount

class BankAccountListView(generics.ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


