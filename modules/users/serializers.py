from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from libs.serializers import DictSerializer

from .models import UserPreference


User = get_user_model()


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


class UserSelfUpdateSerializer(serializers.ModelSerializer):
    """
    用户更新自己信息的序列化器
    """
    class Meta:
        model = User  # 将在视图中动态设置
        fields = ('email', 'first_name', 'last_name')

    def validate_email(self, value):
        # 检查邮箱是否已被其他用户使用
        if User.objects.filter(
                email=value).exclude(
                pk=self.instance.pk).exists():
            raise serializers.ValidationError("该邮箱已被其他用户使用")
        return value


class UserChangePasswordSerializer(DictSerializer):
    """
    用户修改密码序列化器
    """
    old_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="当前密码"
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="新密码"
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="确认新密码"
    )

    def validate_old_password(self, value):
        """验证旧密码是否正确"""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("当前密码不正确")
        return value

    def validate_new_password(self, value):
        """验证新密码强度"""
        user = self.context['request'].user
        try:
            validate_password(value, user)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value

    def validate(self, attrs):
        """验证新密码和确认密码是否一致"""
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'confirm_password': "新密码和确认密码不一致"
            })

        # 检查新密码是否与旧密码相同
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({
                'new_password': "新密码不能与当前密码相同"
            })

        return attrs

    def save(self):
        """保存新密码"""
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return {'message': '密码修改成功'}


class UserSetPasswordSerializer(DictSerializer):
    """
    管理员设置用户密码序列化器
    """
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="新密码"
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        help_text="确认新密码"
    )

    def validate_new_password(self, value):
        """验证新密码强度"""
        # 获取目标用户（从视图中传入）
        target_user = self.context.get('target_user')
        try:
            validate_password(value, target_user)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value

    def validate(self, attrs):
        """验证新密码和确认密码是否一致"""
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'confirm_password': "新密码和确认密码不一致"
            })
        return attrs

    def save(self):
        """保存新密码"""
        target_user = self.context['target_user']
        target_user.set_password(self.validated_data['new_password'])
        target_user.save()
        return {'message': f'用户 {target_user.username} 的密码设置成功'}
