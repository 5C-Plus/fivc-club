from django_filters.rest_framework import (
    filters,
    filterset,
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
    transact_amount__lte = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='lte',
    )
    transact_amount__gte = filters.NumberFilter(
        field_name='transact_amount',
        lookup_expr='gte',
    )
    transact_time__lt = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='lt',
    )
    transact_time__lte = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='lte',
    )
    transact_time__gt = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='gt',
    )
    transact_time__gte = filters.IsoDateTimeFilter(
        field_name='transact_time',
        lookup_expr='gte',
    )

    class Meta:
        model = Transaction
        fields = (
            'club',
            'category',
            'account',
            'transact_audited',
            'transact_amount__lte',
            'transact_amount__gte',
            'transact_time__lt',
            'transact_time__lte',
            'transact_time__gt',
            'transact_time__gte',
        )
