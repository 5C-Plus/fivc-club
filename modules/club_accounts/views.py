from django.db import models
from rest_framework import (
    exceptions,
    viewsets,
)
from libs.permissions import (
    IsAdminOrReadOnly,
)
from libs.viewsets.mixins import (
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
)

from .filters import (
    AccountFilterSet,
    TransactionCategoryFilterSet,
    TransactionFilterSet,
)
from .models import (
    Account,
    TransactionCategory,
    Transaction,
)
from .serializers import (
    AccountSerializer,
    TransactionCategorySerializer,
    TransactionSerializer,
)


class AccountViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = AccountFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Account.objects.select_related(
        'club', 'created_by', 'modified_by',
    ).annotate(
        balance=models.Sum(
            'transactions__transact_amount'
        )
    ).all()
    serializer_class = AccountSerializer


class TransactionCategoryViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = TransactionCategoryFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = TransactionCategory.objects.select_related(
        'club', 'created_by', 'modified_by',
    )
    serializer_class = TransactionCategorySerializer


class TransactionViewSet(
    ProtectedCreateViewSetMixin,
    ProtectedDestroyViewSetMixin,
    viewsets.ModelViewSet,
):
    filterset_class = TransactionFilterSet
    lookup_field = 'uuid'
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Transaction.objects.select_related(
        'category',
        'account',
        # 'account__club',
        'created_by',
        'modified_by',
    ).order_by('-transact_time')
    serializer_class = TransactionSerializer

    def perform_destroy(self, instance):
        if instance.account.is_sealed:
            raise exceptions.PermissionDenied(
                'not allowed to delete transaction in sealed account')

        return super().perform_destroy(instance)
