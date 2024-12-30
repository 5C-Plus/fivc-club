from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class Meeting(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    meeting
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    club = models.ForeignKey(
        'clubs.Club',
        related_name='meetings',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    location = models.TextField(
        default='',
        blank=True,
    )


# class MeetingRole(
#
#     models.Model,
# ):
#     pass
