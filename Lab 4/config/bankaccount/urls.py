from django.urls import path
from .views import BankAccountListView

app_name = 'bankaccount'


urlpatterns = [
    path('accounts/', BankAccountListView.as_view(), name='bankaccount-list-create'),
]