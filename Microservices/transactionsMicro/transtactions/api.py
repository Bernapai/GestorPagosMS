from .serializers import TransactionSerializer
from rest_framework import viewsets, permissions
from .models import Transaction
from .messenger import create_transaction_and_send_messages 

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        create_transaction_and_send_messages(serializer)
