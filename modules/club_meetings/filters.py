from django_filters.rest_framework import (
    filters,
    filterset,
)

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
    MeetingSessionRoleBinding,
)


class MeetingVenueFilterSet(filterset.FilterSet):
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    address_contains = filters.CharFilter(
        field_name='address',
        lookup_expr='contains',
    )

    class Meta:
        model = MeetingVenue
        fields = (
            'club',
            'address',
            'address_contains',
        )


class MeetingFilterSet(filterset.FilterSet):
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    theme_contains = filters.CharFilter(
        field_name='theme',
        lookup_expr='contains',
    )
    time_lt = filters.IsoDateTimeFilter(
        field_name='time',
        lookup_expr='lt',
    )
    time_gt = filters.IsoDateTimeFilter(
        field_name='time',
        lookup_expr='gt',
    )
    time_lte = filters.IsoDateTimeFilter(
        field_name='time',
        lookup_expr='lte',
    )
    time_gte = filters.IsoDateTimeFilter(
        field_name='time',
        lookup_expr='gte',
    )

    class Meta:
        model = Meeting
        fields = (
            'club',
            'theme',
            'theme_contains',
            'time_lt',
            'time_lte',
            'time_gt',
            'time_gte',
        )


class MeetingRoleFilterSet(filterset.FilterSet):
    meeting = filters.UUIDFilter(
        field_name='meeting__uuid',
    )
    meeting_session = filters.UUIDFilter(
        field_name='meeting_session_role_bindings__meeting_session__uuid',
    )
    meeting_session_exclude = filters.UUIDFilter(
        field_name='meeting_session_role_bindings__meeting_session__uuid',
        exclude=True,
    )

    class Meta:
        model = MeetingRole
        fields = (
            'meeting',
            'meeting_session',
            'meeting_session_exclude',
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


class MeetingSessionRoleBindingFilterSet(filterset.FilterSet):
    meeting = filters.UUIDFilter(
        field_name='meeting_session__meeting__uuid',
    )
    meeting_role = filters.UUIDFilter(
        field_name='meeting_role__uuid',
    )
    meeting_session = filters.UUIDFilter(
        field_name='meeting_session__uuid',
    )

    class Meta:
        model = MeetingSessionRoleBinding
        fields = (
            'meeting',
            'meeting_role',
            'meeting_session',
        )
