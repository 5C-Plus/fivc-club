from uuid import uuid1

from django.conf import settings
from django.db import models

from libs.models.mixins import (
    TrackableModelMixin,
    VersionedModelMixin,
)


class WeChatAccount(
    TrackableModelMixin,
    VersionedModelMixin,
    models.Model,
):
    """微信公众号账号信息"""

    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
        verbose_name='UUID',
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='wechat_account',
        on_delete=models.CASCADE,
        db_constraint=False,
        verbose_name='用户',
    )
    openid = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='OpenID',
    )
    unionid = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name='UnionID',
    )
    nickname = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name='昵称',
    )
    avatar_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='头像URL',
    )
    access_token = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='访问令牌',
    )
    refresh_token = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name='刷新令牌',
    )
    expires_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='令牌过期时间',
    )

    class Meta:
        verbose_name = '微信账号'
        verbose_name_plural = verbose_name
