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
    'transactions/categories',
    TransactionCategoryViewSet,
    basename='categories',
)
router.register(
    'transactions',
    TransactionViewSet,
    basename='transactions',
)
router.register(
    'accounts',
    AccountViewSet,
    basename='accounts',
)

urlpatterns = [
    path('', include(router.urls))
]
