from django.apps import apps
from rest_framework import serializers
from libs.serializers import (
    TrackableModelSerializer,
    TrackableCreateModelSerializer,
)

from .models import (
    MeetingVenue,
    Meeting,
    MeetingRole,
    MeetingSession,
    MeetingSessionRoleBinding,
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
            'external',
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
    venue_external = serializers.ReadOnlyField(
        source='venue.external',
        default=None,
    )
    meeting_manager = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'club_participants.Participant').objects.all(),
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
            'venue_external',
            'meeting_manager_name',
        )
        fields = (
            'club',
            'time',
            'theme',
            'notes',
            'venue',
            'meeting_manager',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)

        return super().update(instance, validated_data)


class MeetingSessionSerializer(TrackableModelSerializer):
    class RoleSerializer(serializers.Serializer):
        uuid = serializers.ReadOnlyField(
            source='meeting_role.participant.uuid',
        )
        title = serializers.ReadOnlyField(
            source='meeting_role.title',
        )
        name = serializers.ReadOnlyField(
            source='meeting_role.participant.name',
            default=None,
        )
        intro = serializers.ReadOnlyField(
            source='meeting_role.participant.intro',
            default=None,
        )

    meeting = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Meeting.objects.all(),
    )
    meeting_roles = RoleSerializer(
        source='meeting_session_role_bindings',
        many=True,
        read_only=True,
    )

    class Meta:
        model = MeetingSession
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',
            'modified_time',
            'modified_by',

            'meeting_roles',
        )
        fields = (
            'meeting',
            'name',
            'order',
            'duration',
            'notes',
            'is_highlighted',
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
    participant = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'club_participants.Participant').objects.all(),
        allow_null=True,
        default=None,
    )
    participant_name = serializers.ReadOnlyField(
        source='participant.name',
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

            'participant_name',
        )
        fields = (
            'meeting',
            'title',
            'participant',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change meeting and session
        validated_data.pop('meeting', None)
        # validated_data.pop('meeting_session', None)

        return super().update(instance, validated_data)


class MeetingSessionRoleBindingSerializer(
    TrackableCreateModelSerializer
):
    meeting_role = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=MeetingRole.objects.all(),
    )
    meeting_role_title = serializers.ReadOnlyField(
        source='meeting_role.title',
        default='',
    )
    meeting_role_participant_name = serializers.ReadOnlyField(
        source='meeting_role.participant.name',
        default='',
    )
    meeting_role_participant_intro = serializers.ReadOnlyField(
        source='meeting_role.participant.intro',
        default='',
    )
    meeting_session = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=MeetingSession.objects.all(),
    )

    class Meta:
        model = MeetingSessionRoleBinding
        read_only_fields = (
            'uuid',
            'created_time',
            'created_by',

            'meeting_role_title',
            'meeting_role_participant_name',
            'meeting_role_participant_intro',
        )
        fields = (
            'meeting_role',
            'meeting_session',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        raise AssertionError('not allowed to update')
