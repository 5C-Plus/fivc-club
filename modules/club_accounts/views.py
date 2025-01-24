import pytz

from django.db import models
from django.db.models import functions
from django.http import StreamingHttpResponse
from rest_framework import (
    decorators,
    exceptions,
    response,
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
    TransactionStatisticSerializer,
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
                'not allowed to delete '
                'transaction in sealed account')

        return super().perform_destroy(instance)

    @decorators.action(
        methods=['GET'],
        detail=False,
        serializer_class=TransactionStatisticSerializer,
    )
    def statistic(self, request, *args, **kwargs):
        try:
            # get time zone
            tz = request.query_params.get(
                'transact_time_zone')
            tz = pytz.timezone(tz)
        except pytz.exceptions.Error:
            raise exceptions.ValidationError(
                'invalid timezone offset')

        qs = self.filter_queryset(self.get_queryset())
        qs = qs.annotate(
            transact_date=functions.TruncDate(
                'transact_time', tzinfo=tz)
        )
        qs = qs.values('transact_date').annotate(
            transact_amount=models.Sum('transact_amount'),
        ).values(
            'transact_date',
            'transact_amount',
        ).order_by('transact_date')
        ser = self.get_serializer(qs, many=True)
        return response.Response({'results': ser.data})

    @decorators.action(
        methods=['GET'],
        detail=False,
    )
    def export(self, request, *args, **kwargs):
        def export_streaming(queryset, transact_tz):
            yield '\ufeff'  # write utf-8 boom first
            yield ','.join([
                'Time',
                'Category',
                'Description',
                'Amount',
                'Balance',
            ]) + '\n'

            balance = 0
            for i in queryset.all():
                balance += i.transact_amount
                yield ','.join([
                    f'"{str(i.transact_time.astimezone(transact_tz))}"',
                    f'"{i.category.name}"',
                    f'"{i.description}"',
                    f'"{i.transact_amount}"',
                    f'"{balance}"',
                ]) + '\n'

        try:
            # get time zone
            tz = request.query_params.get(
                'transact_time_zone')
            tz = pytz.timezone(tz)
        except pytz.exceptions.Error:
            raise exceptions.ValidationError(
                'invalid timezone offset')

        qs = self.filter_queryset(self.get_queryset())
        qs = qs.order_by('transact_time')
        resp = StreamingHttpResponse(export_streaming(qs, tz))
        resp['Content-Type'] = 'text/csv'
        resp['Content-Disposition'] = \
            'attachment; filename="accounts.csv"'
        return resp
