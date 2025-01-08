from django.apps import apps
from rest_framework import serializers
from libs.serializers import (
    TrackableModelSerializer
)

from .models import (
    Attendee,
    Membership,
)


class AttendeeSerializer(TrackableModelSerializer):

    class Meta:
        model = Attendee
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',
        )
        fields = (
            'name',
            'intro',
            'picture',
            'title',
            'birthday',
            *read_only_fields,
        )


class MembershipSerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )
    attendee = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'club_members.Attendee').objects.all(),
    )
    attendee_name = serializers.ReadOnlyField(
        source='attendee.name',
        default='',
    )
    attendee_intro = serializers.ReadOnlyField(
        source='attendee.intro',
        default='',
    )
    attendee_picture = serializers.ReadOnlyField(
        source='attendee.picture',
        default=None,
    )
    attendee_birthday = serializers.ReadOnlyField(
        source='attendee.birthday',
        default=None,
    )

    class Meta:
        model = Membership
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'club_name',
            'attendee_name',
            'attendee_intro',
            'attendee_picture',
            'attendee_birthday',
        )
        fields = (
            'club',
            'attendee',
            'type',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)
        # can not change attendee
        validated_data.pop('attendee', None)

        return super().update(instance, validated_data)
