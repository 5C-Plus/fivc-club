import http
import json

from django.contrib.auth import get_user_model
from rest_framework import test


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
