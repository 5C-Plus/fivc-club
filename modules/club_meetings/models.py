from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class MeetingVenue(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    venue
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    club = models.ForeignKey(
        'clubs.Club',
        related_name='meeting_venues',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    address = models.TextField()
    # extra details redirect to external link
    # which might be a video
    extra = models.URLField(
        null=True,
        default=None,
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
    # time = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    # meeting theme
    theme = models.TextField(
        blank=True,
        default='',
    )
    # extra info such as highlights and WOD
    extra = models.TextField(
        blank=True,
        default='',
    )
    # meeting venue
    venue = models.ForeignKey(
        MeetingVenue,
        related_name='meetings',
        on_delete=models.PROTECT,
        db_constraint=False,
        null=True,
        default=None,
    )
    # meeting manager
    meeting_manager = models.ForeignKey(
        'club_participants.Participant',
        related_name='meetings',
        on_delete=models.PROTECT,
        db_constraint=False,
        null=True,
        default=None,
    )

    class Meta:
        unique_together = [
            ('club', 'date')  # one at most a day
        ]

    def save(self, *args, **kwargs):
        if (
                self.venue and
                self.venue.club_id != self.club_id
        ):
            from rest_framework import exceptions
            raise exceptions.PermissionDenied(
                'can not set venue belongs to other club')

        return super().save(*args, **kwargs)


class MeetingSession(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    meeting session
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    meeting = models.ForeignKey(
        Meeting,
        related_name='meeting_sessions',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    # name
    name = models.CharField(
        max_length=255,
    )
    # session order in the meeting
    order = models.FloatField()
    # duration time of this session
    duration = models.DurationField()


class MeetingRole(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    meeting role
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    meeting = models.ForeignKey(
        Meeting,
        related_name='meeting_roles',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    meeting_session = models.ForeignKey(
        MeetingSession,
        related_name='meeting_roles',
        on_delete=models.CASCADE,
        db_constraint=False,
        null=True,
        default=None,
    )
    type_enum = {
        # regular roles -------------------
        'TME': 'Toastmaster Of the Evening',
        'TMD': 'Toastmaster Of the Day',
        'TTM': 'Table Topics Master',
        'IE': 'Individual Evaluator',
        'GE': 'General Evaluator',
        'Timer': 'Timer',
        'AhCounter': 'Ah Counter',
        'Grammarian': 'Grammarian',
        'Photographer': 'Photographer',
        'ItSupport': 'IT Support',

        # special roles -------------------
        'SharingMaster': 'Sharing Master',
        'ContestChair': 'Contest Chair',
        'ElectionChair': 'Election Chair',
        'BallotCounter': 'Ballot Counter',
        'SAA': 'Sergeant At Arms',
    }
    type = models.CharField(
        max_length=32,
        choices=list(type_enum.items()),
    )
    # may be null which indicates that
    # the role has not been taken
    participant = models.ForeignKey(
        'club_participants.Participant',
        related_name='meeting_roles',
        on_delete=models.PROTECT,
        db_constraint=False,
        null=True,
        default=None,
    )

    def save(self, *args, **kwargs):
        if (
                self.meeting_session and
                self.meeting_session.meeting_id != self.meeting_id
        ):
            from rest_framework import exceptions
            raise exceptions.PermissionDenied(
                'can not set role belongs to other meeting')

        return super().save(*args, **kwargs)
