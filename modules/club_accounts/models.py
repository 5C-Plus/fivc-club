from functools import cached_property
from uuid import uuid1

from django.db import models

from libs.models.mixins import (
    # TrackableCreatedModelMixin,
    # VersionedCreatedModelMixin,
    TrackableModelMixin,
    VersionedModelMixin,
)


# class AccountError(Exception):
#     """
#     basic account error
#     """


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
    is_sealed = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = [
            ('club', 'name'),
        ]

    @cached_property
    def balance(self):
        return self.transactions.aggregate(
            balance=models.Sum('transact_amount')
        )['balance'] or 0.0

    def save(self, *args, **kwargs):
        if (
                self.is_sealed and
                self.transactions.filter(
                    transact_audited=False
                ).exists()
        ):
            from rest_framework import exceptions
            raise exceptions.PermissionDenied(
                'can not seal account which has non-audited transaction')

        return super().save(*args, **kwargs)


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
    club = models.ForeignKey(
        'clubs.Club',
        related_name='transaction_categories',
        on_delete=models.PROTECT,
        db_constraint=False,
        null=True,
        default=None,
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
    transact_audited = models.BooleanField(
        default=False
    )
    transact_time = models.DateTimeField()

    # account info --------------------------
    # balance after transaction
    # account_balance = models.DecimalField(
    #     decimal_places=2,
    #     max_digits=12,
    #     null=True,
    #     default=None,
    # )

    def save(self, *args, **kwargs):
        if (
                self.category and
                self.category.club_id != self.account.club_id
        ):
            from rest_framework import exceptions
            raise exceptions.PermissionDenied(
                'can not set category belongs to other clubs')

        return super().save(*args, **kwargs)
