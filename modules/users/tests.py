import http
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status, test


class UserTest(test.APITestCase):
    """
    Test for user related functionality
    """

    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.test_user.is_active = True
        self.test_user.is_staff = True
        self.test_user.save()

    def login_user(self):
        """Helper method to login user via API and get access token"""
        req_url = '/api/users/login/'
        req_data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        return resp.json()['access_token']

    def test_user_login(self):
        req_url = '/api/users/login/'
        req_data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertIn('access_token', resp_data)
        # Check that access_token is not empty
        self.assertTrue(resp_data['access_token'])

    def test_user_login_invalid_credentials(self):
        req_url = '/api/users/login/'
        req_data = {
            'username': 'testuser',
            'password': 'wrongpass',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.UNAUTHORIZED)

    def test_user_logout(self):
        # First login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Then logout
        req_url = '/api/users/logout/'
        resp = self.client.post(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

    def test_get_user_self_authenticated(self):
        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/self/'
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertEqual(resp_data['username'], 'testuser')
        self.assertEqual(resp_data['email'], 'testuser@example.com')

    def test_get_user_self_unauthenticated(self):
        req_url = '/api/users/self/'
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.UNAUTHORIZED)

    def test_update_user_self_authenticated(self):
        """测试已认证用户更新自己的信息"""
        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/self/'
        req_data = {
            'email': 'newemail@example.com',
            'first_name': 'NewFirst',
            'last_name': 'NewLast'
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertEqual(resp_data['email'], 'newemail@example.com')
        self.assertEqual(resp_data['first_name'], 'NewFirst')
        self.assertEqual(resp_data['last_name'], 'NewLast')
        self.assertEqual(
            resp_data['username'],
            'testuser')  # username should not change

        # Verify user was actually updated in database
        self.test_user.refresh_from_db()
        self.assertEqual(self.test_user.email, 'newemail@example.com')
        self.assertEqual(self.test_user.first_name, 'NewFirst')
        self.assertEqual(self.test_user.last_name, 'NewLast')

    def test_update_user_self_partial(self):
        """测试部分更新用户信息"""
        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/self/'
        req_data = {
            'first_name': 'UpdatedFirst'
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertEqual(resp_data['first_name'], 'UpdatedFirst')
        self.assertEqual(
            resp_data['email'],
            'testuser@example.com')  # should remain unchanged

    def test_update_user_self_unauthenticated(self):
        """测试未认证用户更新信息"""
        req_url = '/api/users/self/'
        req_data = {
            'first_name': 'NewFirst'
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.UNAUTHORIZED)

    def test_update_user_self_duplicate_email(self):
        """测试更新为已存在的邮箱"""
        User = get_user_model()
        # 创建另一个用户
        User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )

        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/self/'
        req_data = {
            'email': 'other@example.com'  # 尝试使用已存在的邮箱
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertIn('该邮箱已被其他用户使用', str(resp.data))


class UserPreferenceTest(test.APITestCase):
    """
    Test for user preference functionality
    """

    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )
        self.test_user.is_active = True
        self.test_user.is_staff = True
        self.test_user.save()

    def login_user(self):
        """Helper method to login user via API and get access token"""
        req_url = '/api/users/login/'
        req_data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        return resp.json()['access_token']

    def test_get_preference_authenticated(self):
        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/preference/'
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertIn('content', resp_data)
        self.assertEqual(resp_data['content'], {})  # Default empty dict

    def test_update_preference_authenticated(self):
        # Login via API
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        req_url = '/api/users/preference/'
        req_data = {
            'content': {
                'theme': 'dark',
                'language': 'zh-CN'
            }
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        self.assertEqual(resp_data['content']['theme'], 'dark')
        self.assertEqual(resp_data['content']['language'], 'zh-CN')

    def test_get_preference_unauthenticated(self):
        req_url = '/api/users/preference/'
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.UNAUTHORIZED)

    def test_update_preference_unauthenticated(self):
        req_url = '/api/users/preference/'
        req_data = {
            'content': {
                'theme': 'dark'
            }
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.UNAUTHORIZED)


class UserPasswordTest(test.APITestCase):
    """用户密码相关功能测试"""

    def setUp(self):
        User = get_user_model()

        # 创建普通用户
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='oldpassword123'
        )

        # 创建管理员用户
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='adminpass123',
            is_staff=True
        )

    def login_user(self, username='testuser', password='oldpassword123'):
        """Helper method to login user via API and get access token"""
        req_url = '/api/users/login/'
        req_data = {
            'username': username,
            'password': password,
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        return resp.json()['access_token']

    def login_admin(self):
        """Helper method to login admin user via API and get access token"""
        return self.login_user(username='admin', password='adminpass123')

    def test_change_password_success(self):
        """测试用户成功修改密码"""
        # 登录用户
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:change-password')
        data = {
            'old_password': 'oldpassword123',
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], '密码修改成功')

        # 验证密码已更改
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword456'))

    def test_change_password_wrong_old_password(self):
        """测试旧密码错误的情况"""
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:change-password')
        data = {
            'old_password': 'wrongpassword',
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('当前密码不正确', str(response.data))

    def test_change_password_mismatch_confirmation(self):
        """测试新密码和确认密码不一致的情况"""
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:change-password')
        data = {
            'old_password': 'oldpassword123',
            'new_password': 'newpassword456',
            'confirm_password': 'differentpassword'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('新密码和确认密码不一致', str(response.data))

    def test_change_password_same_as_old(self):
        """测试新密码与旧密码相同的情况"""
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:change-password')
        data = {
            'old_password': 'oldpassword123',
            'new_password': 'oldpassword123',
            'confirm_password': 'oldpassword123'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('新密码不能与当前密码相同', str(response.data))

    def test_change_password_unauthenticated(self):
        """测试未认证用户修改密码"""
        url = reverse('users:change-password')
        data = {
            'old_password': 'oldpassword123',
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_admin_set_password_success(self):
        """测试管理员成功设置用户密码"""
        access_token = self.login_admin()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:set-password', kwargs={'username': 'testuser'})
        data = {
            'new_password': 'adminsetpass123',
            'confirm_password': 'adminsetpass123'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('密码设置成功', response.data['message'])

        # 验证密码已更改
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('adminsetpass123'))

    def test_non_admin_set_password_forbidden(self):
        """测试非管理员用户设置密码被拒绝"""
        access_token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:set-password', kwargs={'username': 'testuser'})
        data = {
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_set_password_user_not_found(self):
        """测试设置不存在用户的密码"""
        access_token = self.login_admin()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        url = reverse('users:set-password', kwargs={'username': 'nonexistent'})
        data = {
            'new_password': 'newpassword456',
            'confirm_password': 'newpassword456'
        }

        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
