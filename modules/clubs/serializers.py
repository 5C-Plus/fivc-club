from libs.serializers import (
    TrackableModelSerializer
)

from .models import (
    Club,
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
            'intro',
            'picture',
            *read_only_fields,
        )
