import datetime
import http
import json
from unittest import mock

from django.contrib.auth import get_user_model
# from django.urls import reverse
from django.utils import timezone
from rest_framework import test
from rest_framework.test import APIClient

from .models import WeChatAccount

User = get_user_model()


class WeChatAuthTest(test.APITestCase):
    """微信认证测试"""

    def setUp(self):
        self.auth_url = '/api/wechat/auth/'
        self.redirect_uri = 'http://example.com/callback'
        self.client = APIClient()

    def test_get_auth_url(self):
        """测试获取微信授权URL"""
        resp = self.client.get(
            self.auth_url,
            {'redirect_uri': self.redirect_uri}
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertIn('auth_url', resp.json())
        auth_url = resp.json()['auth_url']
        self.assertIn('appid=', auth_url)
        self.assertIn(
            'redirect_uri=http%3A%2F%2Fexample.com%2Fcallback',
            auth_url)
        self.assertIn('scope=snsapi_userinfo', auth_url)

    def test_get_auth_url_without_redirect_uri(self):
        """测试获取微信授权URL时未提供redirect_uri"""
        resp = self.client.get(self.auth_url)
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertEqual(resp.json()['detail'], 'redirect_uri is required')

    @mock.patch('urllib.request.urlopen')
    def test_wechat_auth_success(self, mock_urlopen):
        """测试微信认证成功"""
        # Mock 微信API响应
        mock_token_response = mock.MagicMock()
        mock_token_response.read.return_value = json.dumps({
            'access_token': 'test_access_token',
            'refresh_token': 'test_refresh_token',
            'openid': 'test_openid',
            'expires_in': 7200,
        }).encode()

        mock_userinfo_response = mock.MagicMock()
        mock_userinfo_response.read.return_value = json.dumps({
            'openid': 'test_openid',
            'nickname': 'Test User',
            'headimgurl': 'http://example.com/avatar.jpg',
            'unionid': 'test_unionid',
        }).encode()

        # Configure mock to handle context manager
        mock_urlopen.return_value.__enter__.side_effect = [
            mock_token_response,
            mock_userinfo_response,
        ]

        # 发送认证请求
        resp = self.client.post(
            self.auth_url,
            data={'code': 'test_code'},
            format='json'
        )

        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        self.assertIn('access_token', resp.json())

        # 验证数据库中的用户和微信账号
        wechat_account = WeChatAccount.objects.get(openid='test_openid')
        self.assertEqual(wechat_account.nickname, 'Test User')
        self.assertEqual(wechat_account.unionid, 'test_unionid')
        self.assertEqual(
            wechat_account.avatar_url,
            'http://example.com/avatar.jpg')
        self.assertEqual(wechat_account.access_token, 'test_access_token')
        self.assertEqual(wechat_account.refresh_token, 'test_refresh_token')

        user = wechat_account.user
        self.assertEqual(user.username, 'wx_test_openid')
        self.assertTrue(user.is_active)
        self.assertFalse(user.has_usable_password())

    @mock.patch('urllib.request.urlopen')
    def test_wechat_auth_api_error(self, mock_urlopen):
        """测试微信API返回错误"""
        mock_response = mock.MagicMock()
        mock_response.read.return_value = json.dumps({
            'errcode': 40029,
            'errmsg': 'invalid code',
        }).encode()

        # Configure mock to handle context manager
        mock_urlopen.return_value.__enter__.return_value = mock_response

        resp = self.client.post(
            self.auth_url,
            data={'code': 'invalid_code'},
            format='json'
        )

        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn('WeChat API error', resp.json()['detail'])


class WeChatAccountTest(test.APITestCase):
    """微信账号测试"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.wechat_account = WeChatAccount.objects.create(
            user=self.user,
            openid='test_openid',
            nickname='Test User',
            avatar_url='http://example.com/avatar.jpg',
            access_token='test_access_token',
            refresh_token='test_refresh_token',
            expires_at=timezone.now() + datetime.timedelta(hours=2),
        )
        self.account_url = '/api/wechat/account/'

    def test_get_account_info_authenticated(self):
        """测试获取已认证用户的微信账号信息"""
        self.client.force_authenticate(user=self.user)
        resp = self.client.get(self.account_url)
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

        data = resp.json()
        self.assertEqual(data['openid'], 'test_openid')
        self.assertEqual(data['nickname'], 'Test User')
        self.assertEqual(data['avatar_url'], 'http://example.com/avatar.jpg')

    def test_get_account_info_unauthenticated(self):
        """测试未认证用户获取微信账号信息"""
        resp = self.client.get(self.account_url)
        self.assertEqual(resp.status_code, http.HTTPStatus.UNAUTHORIZED)

    def test_get_account_info_no_wechat_account(self):
        """测试获取没有绑定微信账号的用户信息"""
        user2 = User.objects.create_user(
            username='testuser2',
            password='testpass123'
        )
        self.client.force_authenticate(user=user2)
        resp = self.client.get(self.account_url)
        self.assertEqual(resp.status_code, http.HTTPStatus.NOT_FOUND)
