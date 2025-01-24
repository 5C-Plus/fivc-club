from libs.serializers import (
    TrackableModelSerializer
)

from .models import (
    Club,
    Program,
)


class ClubSerializer(TrackableModelSerializer):

    class Meta:
        model = Club
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',
        )
        fields = (
            'name',
            'alias',
            'intro',
            'picture',
            *read_only_fields,
        )


class ProgramSerializer(TrackableModelSerializer):
    class Meta:
        model = Program
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',
        )
        fields = (
            'name',
            'alias',
            'description',
            *read_only_fields,
        )
