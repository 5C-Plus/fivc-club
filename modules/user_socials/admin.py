from django.contrib import admin

from .models import WeChatAccount


@admin.register(WeChatAccount)
class WeChatAccountAdmin(admin.ModelAdmin):
    """微信账号管理"""

    list_display = (
        'user',
        'openid',
        'nickname',
        'created_time',
        'modified_time',
    )
    list_filter = (
        'created_time',
        'modified_time',
    )
    search_fields = (
        'user__username',
        'openid',
        'nickname',
    )
    readonly_fields = (
        'uuid',
        'created_time',
        'modified_time',
    )
