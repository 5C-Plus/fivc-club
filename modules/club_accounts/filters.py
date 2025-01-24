from django_filters.rest_framework import (
    filters,
    filterset,
)

from libs.filters import (
    DummyFilter
)
from .models import (
    Account,
    TransactionCategory,
    Transaction,
)


class AccountFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    club_name = filters.CharFilter(
        field_name='club__name',
    )

    class Meta:
        model = Account
        fields = (
            'name',
            'name_contains',
            'club',
            'club_name',
        )


class TransactionCategoryFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    club_name = filters.CharFilter(
        field_name='club__name',
    )

    class Meta:
        model = TransactionCategory
        fields = (
            'name',
            'name_contains',
            'club',
            'club_name',
        )


class TransactionFilterSet(filterset.FilterSet):
    club = filters.UUIDFilter(
        field_name='account__club__uuid',
    )
    category = filters.UUIDFilter(
        field_name='category__uuid',
    )
    account = filters.UUIDFilter(
        field_name='account__uuid',
    )
    transact_amount_lt = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='lt',
    )
    transact_amount_lte = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='lte',
    )
    transact_amount_gt = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='gt',
    )
    transact_amount_gte = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='gte',
    )
    transact_time_lt = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='lt',
    )
    transact_time_lte = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='lte',
    )
    transact_time_gt = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='gt',
    )
    transact_time_gte = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='gte',
    )
    # for statistic api
    transact_time_zone = DummyFilter()

    class Meta:
        model = Transaction
        fields = (
            'club',
            'category',
            'account',
            'transact_audited',
            'transact_amount_lt',
            'transact_amount_lte',
            'transact_amount_gt',
            'transact_amount_gte',
            'transact_time_lt',
            'transact_time_lte',
            'transact_time_gt',
            'transact_time_gte',
            'transact_time_zone',
        )
