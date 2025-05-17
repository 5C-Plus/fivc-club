from rest_framework import serializers

from libs.serializers import DictSerializer

from .models import UserPreference


class UserPreferenceSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
    )

    class Meta:
        model = UserPreference
        read_only_fields = (
            'uuid',
            'user',
            'created_time',
            'modified_time',
        )
        fields = (
            'content',
            *read_only_fields,
        )


class UserLoginSerializer(DictSerializer):
    username = serializers.CharField(
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
    )
    access_token = serializers.CharField(
        read_only=True,
    )


class UserSelfSerializer(DictSerializer):
    username = serializers.CharField(
        read_only=True,
    )
    email = serializers.CharField(
        read_only=True,
    )
    first_name = serializers.CharField(
        read_only=True,
    )
    last_name = serializers.CharField(
        read_only=True,
    )
    is_staff = serializers.BooleanField(
        read_only=True,
    )
    is_active = serializers.BooleanField(
        read_only=True,
    )
    date_joined = serializers.DateTimeField(
        read_only=True,
    )
