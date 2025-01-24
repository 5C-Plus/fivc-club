from django.apps import apps
from rest_framework import serializers
from libs.serializers import (
    TrackableModelSerializer
)

from .models import (
    Participant,
    ParticipantTitle,
    Member,
)


class ParticipantSerializer(TrackableModelSerializer):
    class ClubSerializer(serializers.Serializer):
        uuid = serializers.UUIDField(
            source='club.uuid',
        )
        name = serializers.CharField(
            source='club.name',
        )
        alias = serializers.CharField(
            source='club.alias',
        )

    class TitleSerializer(serializers.Serializer):
        uuid = serializers.UUIDField(
            source='uuid',
        )
        name = serializers.SerializerMethodField()

        @staticmethod
        def get_name(instance):
            if not instance.level:
                return instance.program.name

            return f'{instance.program.name}{str(instance.level)}'

    clubs = ClubSerializer(
        source='members',
        many=True,
        read_only=True,
    )
    titles = TitleSerializer(
        source='participant_titles',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Participant
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'clubs',
            'titles',
        )
        fields = (
            'name',
            'intro',
            'picture',
            'title',
            'birthday',
            *read_only_fields,
        )


class ParticipantTitleSerializer(
    TrackableModelSerializer
):
    program = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'clubs.Program').objects.all()
    )
    program_name = serializers.ReadOnlyField(
        source='program.name',
        default='',
    )
    participant = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Participant.objects.all(),
    )
    participant_name = serializers.ReadOnlyField(
        source='participant.name',
        default='',
    )

    class Meta:
        model = ParticipantTitle
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'program_name',
            'participant_name',
        )
        fields = (
            'program',
            'participant',
            'level',
            *read_only_fields,
        )


class MemberSerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model(
            'clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )
    participant = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Participant.objects.all(),
    )
    participant_name = serializers.ReadOnlyField(
        source='participant.name',
        default='',
    )
    participant_intro = serializers.ReadOnlyField(
        source='participant.intro',
        default='',
    )
    # participant_picture = serializers.ReadOnlyField(
    #     source='participant.picture',
    #     default=None,
    # )
    participant_birthday = serializers.ReadOnlyField(
        source='participant.birthday',
        default=None,
    )

    class Meta:
        model = Member
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'club_name',
            'participant_name',
            'participant_intro',
            # 'participant_picture',
            'participant_birthday',
        )
        fields = (
            'club',
            'participant',
            'type',
            'description',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)
        # can not change participant
        validated_data.pop('participant', None)

        return super().update(instance, validated_data)
