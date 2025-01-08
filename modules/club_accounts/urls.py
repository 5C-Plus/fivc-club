from django.urls import path, include
from libs.routers import DefaultRouter

from .views import (
    AccountViewSet,
    TransactionCategoryViewSet,
    TransactionViewSet,
)

app_name = 'club_accounts'

router = DefaultRouter()
router.register(
    'accounts/transactions/categories',
    TransactionCategoryViewSet,
    basename='account_transaction_categories',
)
router.register(
    'accounts/transactions',
    TransactionViewSet,
    basename='account_transactions',
)
router.register(
    'accounts',
    AccountViewSet,
    basename='accounts',
)

urlpatterns = [
    path('', include(router.urls))
]
