import http
import json
import unittest.mock

from rest_framework import (
    test,
    reverse,
)


class AccountTest(test.APITestCase):
    """
    test for account
    """

    fixtures = ['test_clubs.json', 'test_accounts.json']

    @unittest.mock.patch(
        'modules.club_accounts.views.'
        'AccountViewSet.permission_classes', [])
    def test_create_account(self):
        req_url = reverse.reverse('club_accounts:accounts-list')
        req_data = {
            'name': 'Test Account 1',
            'club': '23aa0182-c5f7-11ef-8557-ba4b1618bd02',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.CREATED)

        resp_data = resp.json()
        self.assertEqual(resp_data['name'], 'Test Account 1')
        self.assertEqual(resp_data['balance'], 0.0)

    @unittest.mock.patch(
        'modules.club_accounts.views.'
        'AccountViewSet.permission_classes', [])
    def test_create_account_same_name(self):
        req_url = reverse.reverse('club_accounts:accounts-list')
        req_data = {
            # create with name that is already exist in the same club
            'name': 'Default',
            'club': '23aa0182-c5f7-11ef-8557-ba4b1618bd02',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.BAD_REQUEST)

    @unittest.mock.patch(
        'modules.club_accounts.views.'
        'AccountViewSet.permission_classes', [])
    def test_create_account_change_club(self):
        req_url = reverse.reverse('club_accounts:accounts-detail', [
            '97ecc0aa-c6bc-11ef-a407-ba4b1618bd02'
        ])
        req_data = {
            # create with name that is already exist in the same club
            'name': 'Default2',
            'club': '23aa0182-c5f7-11ef-8557-ba4b1618bd03',
        }
        resp = self.client.patch(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)

        resp_data = resp.json()
        # name will be changed
        self.assertEqual(resp_data['name'], 'Default2')
        # club will NOT be changed
        self.assertEqual(
            resp_data['club'],
            '23aa0182-c5f7-11ef-8557-ba4b1618bd02')

    def test_list_account(self):
        req_url = reverse.reverse('club_accounts:accounts-list')
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)
        resp_data = resp.json()
        self.assertIn('count', resp_data)
        self.assertEqual(resp_data['count'], 1)
