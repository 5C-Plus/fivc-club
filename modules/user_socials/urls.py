from django.urls import path

from .views import (
    WeChatAuthView,
    WeChatAccountView,
)

app_name = 'user_socials'

urlpatterns = [
    path(
        'wechat/auth/',
        WeChatAuthView.as_view(),
        name='wechat_auth'),
    path(
        'wechat/account/',
        WeChatAccountView.as_view(),
        name='wechat_account'),
]
