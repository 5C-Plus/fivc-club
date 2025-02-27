from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    TrackableCreatedModelMixin,
    VersionedModelMixin,
    VersionedCreatedModelMixin,
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
    external = models.URLField(
        max_length=4096,
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
    time = models.DateTimeField()
    # name of the meeting
    name = models.CharField(
        max_length=64,
        blank=True,
        default='',
    )
    # meeting theme
    theme = models.TextField(
        blank=True,
        default='',
    )
    # notes such as highlights and WOD
    notes = models.TextField(
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
            ('club', 'name')
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
    # if duration is 0 make it as a wrap-up session
    duration = models.DurationField()
    # notes such as highlights and WOD
    notes = models.TextField(
        blank=True,
        default='',
    )
    # if is highlighted
    is_highlighted = models.BooleanField(
        default=False,
    )


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
    title = models.CharField(
        max_length=64,
        default='',
        blank=True,
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


class MeetingSessionRoleBinding(
    TrackableCreatedModelMixin,
    VersionedCreatedModelMixin,
    models.Model,
):
    """
    meeting role and session binding
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    meeting_role = models.ForeignKey(
        MeetingRole,
        related_name='meeting_session_role_bindings',
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    meeting_session = models.ForeignKey(
        MeetingSession,
        related_name='meeting_session_role_bindings',
        on_delete=models.CASCADE,
        db_constraint=False,
    )

    class Meta:
        unique_together = [
            ('meeting_role', 'meeting_session'),
        ]

    def save(self, *args, **kwargs):
        if (
            self.meeting_role.meeting_id !=
            self.meeting_session.meeting_id
        ):
            from rest_framework import exceptions
            raise exceptions.PermissionDenied(
                'can not bind role and session '
                'which belong to different meeting')

        return super().save(*args, **kwargs)
