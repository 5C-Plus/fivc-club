from rest_framework import serializers

from .models import WeChatAccount


class WeChatAccountSerializer(serializers.ModelSerializer):
    """微信账号序列化器"""

    user = serializers.ReadOnlyField(
        source='user.username',
    )

    class Meta:
        model = WeChatAccount
        read_only_fields = (
            'uuid',
            'user',
            'openid',
            'unionid',
            'nickname',
            'avatar_url',
            'access_token',
            'refresh_token',
            'expires_at',
            'created_time',
            'modified_time',
        )
        fields = read_only_fields


class WeChatAuthSerializer(serializers.Serializer):
    """微信认证序列化器"""

    code = serializers.CharField(
        required=True,
        write_only=True,
    )
    state = serializers.CharField(
        required=False,
        write_only=True,
    )
    access_token = serializers.CharField(
        read_only=True,
    )
