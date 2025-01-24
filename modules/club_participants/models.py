from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class Participant(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    participants
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
    # any description to help VPM
    # description = models.TextField(
    #     blank=True,
    #     default='',
    # )
    birthday = models.DateField(
        null=True,
        default=None,
    )


class ParticipantTitle(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    program = models.ForeignKey(
        'clubs.Program',
        related_name='participant_titles',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    participant = models.ForeignKey(
        Participant,
        related_name='participant_titles',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    level = models.PositiveIntegerField(
        null=True,
        default=None
    )

    class Meta:
        unique_together = [
            ('program', 'participant'),
        ]


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
    participant = models.ForeignKey(
        Participant,
        related_name='members',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    type_enum = {
        'President': 'President',
        'VPE': 'Vice President Education',
        'VPM': 'Vice President Membership',
        'VPPR': 'Vice President Public Relationship',
        'Secretary': 'Secretary',
        'Treasurer': 'Treasurer',
        'SAA': 'Sergeant At Arms',
        'IPP': 'Immediate Past President',
        None: 'None Officer',
    }
    type = models.CharField(
        max_length=32,
        choices=list(type_enum.items()),
        null=True,
        default=None,
    )
    description = models.TextField(
        blank=True,
        default='',
    )

    class Meta:
        unique_together = [
            ('club', 'participant'),
            ('club', 'type'),
        ]
