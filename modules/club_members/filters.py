from django_filters.rest_framework import (
    filters,
    filterset,
)

from .models import (
    Attendee,
    Membership,
)


class AttendeeFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )

    class Meta:
        model = Attendee
        fields = (
            'name',
            'name_contains',
        )


class MembershipFilterSet(filterset.FilterSet):
    type_isnull = filters.BooleanFilter(
        field_name='type',
        lookup_expr='isnull'
    )
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    attendee_name = filters.CharFilter(
        field_name='attendee__name'
    )
    attendee_name_contains = filters.CharFilter(
        field_name='attendee__name',
        lookup_expr='contains',
    )

    class Meta:
        model = Membership
        fields = (
            'type',
            'type_isnull',
            'club',
            'attendee_name',
            'attendee_name_contains',
        )
