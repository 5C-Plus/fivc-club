from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    # TrackableCreatedModelMixin,
    # VersionedCreatedModelMixin,
    TrackableModelMixin,
    VersionedModelMixin,
)


class Account(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    account
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    club = models.ForeignKey(
        'clubs.Club',
        related_name='accounts',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    name = models.CharField(
        max_length=64,
        default='default',
    )
    description = models.TextField(
        blank=True,
        default='',
    )

    class Meta:
        unique_together = [
            ('club', 'name'),
        ]


class TransactionCategory(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    transaction category
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    name = models.CharField(
        unique=True,
        max_length=64,
        default='default',
    )
    description = models.TextField(
        blank=True,
        default='',
    )


class Transaction(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """
    account transaction
    """
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    account = models.ForeignKey(
        Account,
        related_name='transactions',
        on_delete=models.PROTECT,
        db_constraint=False,
    )
    category = models.ForeignKey(
        TransactionCategory,
        related_name='transactions',
        on_delete=models.PROTECT,
        db_constraint=False,
        null=True,
        default=None,
    )
    description = models.TextField(
        blank=True,
        default='',
    )
    # transaction info ----------------------
    transact_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    transact_time = models.DateTimeField()
    # account info --------------------------
    # balance after transaction
    account_balance = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
