from django.apps import apps
from rest_framework import (
    exceptions,
    serializers,
)
from libs.serializers import (
    TrackableModelSerializer,
)

from .models import (
    Account,
    TransactionCategory,
    Transaction,
)


class AccountSerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model('clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Account
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'club_name',
            'balance',
        )
        fields = (
            'club',
            'name',
            'description',
            'is_sealed',
            *read_only_fields,
        )

    @staticmethod
    def get_balance(instance):
        return getattr(instance, 'balance') or 0.0

    def update(self, instance, validated_data):
        if instance.is_sealed:
            raise exceptions.PermissionDenied(
                'account is sealed')

        # can not change club
        validated_data.pop('club', None)

        return super().update(instance, validated_data)


class TransactionCategorySerializer(TrackableModelSerializer):
    club = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=apps.get_model('clubs.Club').objects.all(),
    )
    club_name = serializers.ReadOnlyField(
        source='club.name',
        default='',
    )

    class Meta:
        model = TransactionCategory
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'club_name',
        )
        fields = (
            'club',
            'name',
            'description',
            *read_only_fields,
        )

    def update(self, instance, validated_data):
        # can not change club
        validated_data.pop('club', None)

        return super().update(instance, validated_data)


class TransactionSerializer(TrackableModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=TransactionCategory.objects.all(),
        allow_null=True,
        default=None,
    )
    category_name = serializers.ReadOnlyField(
        source='category.name',
        default='',
    )
    account = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Account.objects.all(),
    )
    account_name = serializers.ReadOnlyField(
        source='account.name',
        default='',
    )

    class Meta:
        model = Transaction
        read_only_fields = (
            'uuid',
            'created_by',
            'created_time',
            'modified_by',
            'modified_time',

            'category_name',
            'account_name',
            # 'account_balance',
        )
        fields = (
            'category',
            'account',

            'description',

            'transact_audited',
            'transact_amount',
            'transact_time',

            *read_only_fields,
        )

    def update(self, instance, validated_data):
        if instance.account.is_sealed:
            raise exceptions.PermissionDenied(
                'account is sealed')

        if instance.transact_audited:
            # can not change transcat info after being audited
            validated_data.pop('transact_audited', None)
            validated_data.pop('transact_amount', None)
            validated_data.pop('transact_time', None)

        # can not change account
        validated_data.pop('account', None)

        return super().update(instance, validated_data)
