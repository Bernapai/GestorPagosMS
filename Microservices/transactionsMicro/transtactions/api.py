from .serializers import TransactionSerializer
from rest_framework import viewsets, permissions
from .models import Transaction

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.AllowAny]
