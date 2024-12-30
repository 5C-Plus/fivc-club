from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class Visitor(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    visitor
    """

    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
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
    # any extra title this person possesses
    title = models.TextField(
        null=True,
        default=None,
    )
    birthday = models.DateField(
        null=True,
        default=None,
    )


class Member(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    member
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    club = models.ForeignKey(
        'clubs.Club',
        related_name='members',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    visitor = models.ForeignKey(
        Visitor,
        related_name='members',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    officer = models.TextField(
        max_length=64,
        null=True,
        default=None,
    )

    class Meta:
        unique_together = [
            ('club', 'visitor'),
            ('club', 'officer'),
        ]
