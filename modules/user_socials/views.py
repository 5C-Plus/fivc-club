import datetime
import json
import logging
import urllib.parse
import urllib.request

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import (
    # exceptions,
    permissions,
    response,
    status,
    views,
)

from .models import WeChatAccount
from .serializers import (
    WeChatAccountSerializer,
    WeChatAuthSerializer,
)

logger = logging.getLogger(__name__)
User = get_user_model()


class WeChatAuthView(views.APIView):
    """微信认证视图"""

    permission_classes = ()

    def get(self, request, *args, **kwargs):
        """获取微信授权URL"""
        redirect_uri = request.query_params.get('redirect_uri')
        if not redirect_uri:
            return response.Response(
                {'detail': 'redirect_uri is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        params = {
            'appid': getattr(settings, 'WECHAT_APP_ID', 'your_app_id'),
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'scope': 'snsapi_userinfo',
            'state': 'STATE',  # 可以根据需要生成随机状态
        }
        auth_url = (
            'https://open.weixin.qq.com/connect/oauth2/authorize?' +
            urllib.parse.urlencode(params, quote_via=urllib.parse.quote) +
            '#wechat_redirect'
        )
        return response.Response({'auth_url': auth_url})

    def post(self, request, *args, **kwargs):
        """处理微信回调，获取用户信息"""
        ser = WeChatAuthSerializer(
            data=request.data,
            context=self.get_renderer_context())
        ser.is_valid(raise_exception=True)
        ser_data = ser.validated_data

        # 获取access_token
        params = {
            'appid': getattr(
                settings,
                'WECHAT_APP_ID',
                'your_app_id'),
            'secret': getattr(
                settings,
                'WECHAT_APP_SECRET',
                'your_app_secret'),
            'code': ser_data['code'],
            'grant_type': 'authorization_code',
        }
        token_url = (
            'https://api.weixin.qq.com/sns/oauth2/access_token?' +
            urllib.parse.urlencode(params)
        )

        try:
            with urllib.request.urlopen(token_url) as f:
                token_data = json.loads(f.read().decode())
        except Exception as e:
            logger.error(f'Failed to get access token: {e}')
            return response.Response(
                {'detail': 'WeChat API error: Failed to get access token'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'errcode' in token_data:
            return response.Response(
                {'detail': f"WeChat API error: {token_data['errmsg']}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 获取用户信息
        params = {
            'access_token': token_data['access_token'],
            'openid': token_data['openid'],
            'lang': 'zh_CN',
        }
        userinfo_url = (
            'https://api.weixin.qq.com/sns/userinfo?' +
            urllib.parse.urlencode(params)
        )

        try:
            with urllib.request.urlopen(userinfo_url) as f:
                userinfo_data = json.loads(f.read().decode())
        except Exception as e:
            logger.error(f'Failed to get user info: {e}')
            return response.Response(
                {'detail': 'WeChat API error: Failed to get user info'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'errcode' in userinfo_data:
            return response.Response(
                {'detail': f"WeChat API error: {userinfo_data['errmsg']}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 先创建或获取用户
        username = f"wx_{userinfo_data['openid']}"
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username)
            user.set_unusable_password()
            user.save()

        # 创建或更新微信账号
        wechat_account, created = WeChatAccount.objects.update_or_create(
            openid=userinfo_data['openid'],
            defaults={
                'user': user,
                'unionid': userinfo_data.get('unionid'),
                'nickname': userinfo_data['nickname'],
                'avatar_url': userinfo_data['headimgurl'],
                'access_token': token_data['access_token'],
                'refresh_token': token_data['refresh_token'],
                'expires_at': timezone.now() + datetime.timedelta(
                    seconds=token_data['expires_in']
                ),
            }
        )

        # 登录用户
        from django.contrib.auth import login
        login(request, user)

        if not request.session.session_key:
            request.session.create()

        return response.Response({
            'access_token': request.session.session_key,
        })


class WeChatAccountView(views.APIView):
    """微信账号视图"""

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """获取当前用户的微信账号信息"""
        try:
            wechat_account = request.user.wechat_account
        except WeChatAccount.DoesNotExist:
            return response.Response(
                {'detail': 'WeChat account not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        ser = WeChatAccountSerializer(
            instance=wechat_account,
            context=self.get_renderer_context()
        )
        return response.Response(ser.data)
