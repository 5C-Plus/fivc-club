from django_filters.rest_framework import (
    filters,
    filterset,
)

from .models import (
    Participant,
    ParticipantTitle,
    Member,
)


class ParticipantFilterSet(filterset.FilterSet):
    name_contains = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )
    club = filters.UUIDFilter(
        field_name='members__club__uuid',
    )
    club_exclude = filters.UUIDFilter(
        field_name='members__club__uuid',
        exclude=True,
    )

    class Meta:
        model = Participant
        fields = (
            'name',
            'name_contains',
            'club',
            'club_exclude',
        )


class ParticipantTitleFilterSet(filterset.FilterSet):
    program = filters.UUIDFilter(
        field_name='program__uuid',
    )
    program_exclude = filters.UUIDFilter(
        field_name='program__uuid',
        exclude=True,
    )
    participant = filters.UUIDFilter(
        field_name='participant__uuid',
    )

    class Meta:
        model = ParticipantTitle
        fields = (
            'program',
            'program_exclude',
            'participant',
            'level',
        )


class MemberFilterSet(filterset.FilterSet):
    type_isnull = filters.BooleanFilter(
        field_name='type',
        lookup_expr='isnull'
    )
    club = filters.UUIDFilter(
        field_name='club__uuid',
    )
    participant_name = filters.CharFilter(
        field_name='participant__name'
    )
    participant_name_contains = filters.CharFilter(
        field_name='participant__name',
        lookup_expr='contains',
    )

    class Meta:
        model = Member
        fields = (
            'type',
            'type_isnull',
            'club',
            'participant_name',
            'participant_name_contains',
        )
