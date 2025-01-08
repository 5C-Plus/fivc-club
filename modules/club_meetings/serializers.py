from django.apps import apps
from rest_framework import serializers
from libs.serializers import (
    TrackableModelSerializer,
)

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
)


class MeetingVenueSerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )

    class Meta:
        model = MeetingVenue
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',
            'modified_time',
            'modified_by',

            'club_name',
        )
        fields = (
            'club',
            'address',
            'extra',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)

        return super().update(instance, validated_data)


class MeetingSerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )
    venue = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=MeetingVenue.objects.all(),
        allow_null=True,
        default=None,
    )
    venue_address = serializers.ReadOnlyField(
        source='venue.address',
        default='',
    )
    venue_extra = serializers.ReadOnlyField(
        source='venue.extra',
        default=None,
    )
    meeting_manager = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'club_members.Attendee').objects.all(),
        allow_null=True,
        default=None,
    )
    meeting_manager_name = serializers.ReadOnlyField(
        source='meeting_manager.name',
        default='',
    )

    class Meta:
        model = Meeting
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',
            'modified_time',
            'modified_by',

            'club_name',
            'venue_address',
            'venue_extra',
            'meeting_manager_name',
        )
        fields = (
            'club',
            'date',
            'time',
            'theme',
            'extra',
            'venue',
            'meeting_manager',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)

        return super().update(instance, validated_data)


class MeetingSessionSerializer(TrackableModelSerializer):
    meeting = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Meeting.objects.all(),
    )

    class Meta:
        model = MeetingSession
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',
            'modified_time',
            'modified_by',
        )
        fields = (
            'meeting',
            'name',
            'order',
            'duration',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change meeting
        validated_data.pop('meeting', None)

        return super().update(instance, validated_data)


class MeetingRoleSerializer(TrackableModelSerializer):
    meeting = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Meeting.objects.all(),
    )
    meeting_session = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=MeetingSession.objects.all(),
    )
    attendee = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'club_members.Attendee').objects.all(),
        allow_null=True,
        default=None,
    )
    attendee_name = serializers.ReadOnlyField(
        source='attendee.name',
        default='',
    )

    class Meta:
        model = MeetingRole
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',
            'modified_time',
            'modified_by',

            'attendee_name',
        )
        fields = (
            'meeting',
            'meeting_session',
            'type',
            'attendee',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change meeting and session
        validated_data.pop('meeting', None)
        validated_data.pop('meeting_session', None)

        return super().update(instance, validated_data)
