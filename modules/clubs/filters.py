from django_filters.rest_framework import (
    filters,
    filterset,
)

from .models import Club, Program


class ClubFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )

    class Meta:
        model = Club
        fields = (
            'name',
            'name_contains',
        )


class ProgramFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )
    alias_contains = filters.CharFilter(
        field_name='alias',
        lookup_expr='contains',
    )

    class Meta:
        model = Program
        fields = (
            'name',
            'name_contains',
            'alias',
            'alias_contains',
        )
