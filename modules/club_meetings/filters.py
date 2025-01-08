from django_filters.rest_framework import (
    filters,
    filterset,
)

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
)


class MeetingVenueFilterSet(filterset.FilterSet):
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )

    class Meta:
        model = MeetingVenue
        fields = (
            'club',
        )


class MeetingFilterSet(filterset.FilterSet):
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    theme_contains = filters.CharFilter(
        field_name='theme',
        lookup_expr='contains',
    )
    date_lt = filters.DateFilter(
        field_name='date',
        lookup_expr='lt',
    )
    date_gt = filters.DateFilter(
        field_name='date',
        lookup_expr='gt',
    )
    date_lte = filters.DateFilter(
        field_name='date',
        lookup_expr='lte',
    )
    date_gte = filters.DateFilter(
        field_name='date',
        lookup_expr='gte',
    )

    class Meta:
        model = Meeting
        fields = (
            'club',
            'theme',
            'theme_contains',
            'date_lt',
            'date_lte',
            'date_gt',
            'date_gte',
        )


class MeetingSessionFilterSet(filterset.FilterSet):
    meeting = filters.UUIDFilter(
        field_name='meeting__uuid',
    )

    class Meta:
        model = MeetingSession
        fields = (
            'meeting',
        )


class MeetingRoleFilterSet(filterset.FilterSet):
    meeting = filters.UUIDFilter(
        field_name='meeting__uuid',
    )
    meeting_session = filters.UUIDFilter(
        field_name='meeting_session__uuid',
    )
    meeting_session_isnull = filters.BooleanFilter(
        field_name='meeting_session',
        lookup_expr='isnull',
    )

    class Meta:
        model = MeetingRole
        fields = (
            'meeting',
            'meeting_session',
        )
