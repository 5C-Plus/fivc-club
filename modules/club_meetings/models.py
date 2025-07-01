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

    def clone(self, **kwargs):
        init_kwargs = {
            'time': self.time,
            'name': self.name,
            'theme': self.theme,
            'notes': self.notes,
            'venue': self.venue,
            'meeting_manager': self.meeting_manager,
        }
        for k, v in init_kwargs.items():
            if k in kwargs:
                init_kwargs[k] = kwargs[k]

        instance = self.__class__(
            uuid=uuid1(),
            club=self.club,
            **init_kwargs,
        )
        instance.save()

        # clone meeting sessions
        session_old_2_new = {}
        for session_old in self.meeting_sessions.all():
            session_new = session_old.clone(meeting=instance)
            session_old_2_new[session_old.id] = session_new.id

        # clone meeting roles
        role_old_2_new = {}
        for role_old in self.meeting_roles.all():
            role_new = role_old.clone(meeting=instance)
            role_old_2_new[role_old.id] = role_new.id

        # clone meeting session role bindings
        binding_cls = MeetingSessionRoleBinding
        binding_new = []
        for binding_old in binding_cls.objects.filter(
            meeting_session__meeting=self,
            meeting_role__meeting=self,
        ).distinct():
            binding_session_new = session_old_2_new.get(
                binding_old.meeting_session_id
            )
            binding_role_new = role_old_2_new.get(
                binding_old.meeting_role_id
            )
            binding_new.append(binding_cls(
                uuid=uuid1(),
                meeting_role_id=binding_role_new,
                meeting_session_id=binding_session_new,
            ))
        binding_cls.objects.bulk_create(binding_new)

        return instance


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

    def clone(self, **kwargs):
        init_kwargs = {
            'name': self.name,
            'order': self.order,
            'duration': self.duration,
            'notes': self.notes,
            'is_highlighted': self.is_highlighted,
            'meeting': self.meeting,
        }
        for k, v in init_kwargs.items():
            if k in kwargs:
                init_kwargs[k] = kwargs[k]

        instance = self.__class__(
            uuid=uuid1(),
            **init_kwargs,
        )
        instance.save()
        return instance


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

    def clone(self, **kwargs):
        init_kwargs = {
            'title': self.title,
            'participant': self.participant,
            'meeting': self.meeting,
        }
        for k, v in init_kwargs.items():
            if k in kwargs:
                init_kwargs[k] = kwargs[k]

        instance = self.__class__(
            uuid=uuid1(),
            **init_kwargs
        )
        instance.save()
        return instance


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
