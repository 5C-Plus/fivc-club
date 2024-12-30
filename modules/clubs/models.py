from uuid import uuid1
from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class Club(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    club
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    # name
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    intro = models.TextField(
        blank=True,
        default='',
    )
    picture = models.ImageField(
        null=True,
        default=None,
    )
    # club birthday
    birthday = models.DateField(
        null=True,
        default=None,
    )

    def __str__(self):
        return self.name
