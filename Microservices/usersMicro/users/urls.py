from rest_framework import routers
from .api import TransactionViewSet

transactionRouter = routers.DefaultRouter()

transactionRouter.register('api/transaction', TransactionViewSet, 'transaction')

urlpatterns = transactionRouter.urls