from uuid import uuid1

from django.conf import settings
from django.db import models

from libs.models.mixins import (
    VersionedModelMixin,
)


class UserPreference(
    # TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='preference',
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    content = models.JSONField(
        default=dict,
    )
