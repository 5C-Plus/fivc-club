import http
import json
import unittest.mock

from rest_framework import (
    test,
    reverse,
)


class ClubTest(test.APITestCase):
    """
    test for club
    """

    fixtures = ['test_clubs.json']

    @unittest.mock.patch(
        'modules.clubs.views.ClubViewSet.permission_classes', [])
    def test_create_club(self):
        req_url = reverse.reverse('clubs:clubs-list')
        req_data = {
            'name': 'Test Club 1',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.CREATED)

        resp_data = resp.json()
        self.assertEqual(resp_data['name'], 'Test Club 1')

    def test_list_club(self):
        req_url = reverse.reverse('clubs:clubs-list')
        resp = self.client.get(req_url)
        self.assertEqual(
            resp.status_code, http.HTTPStatus.OK)
        resp_data = resp.json()
        self.assertIn('count', resp_data)
        self.assertEqual(resp_data['count'], 2)
