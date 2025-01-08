import http
import json
import unittest.mock

from rest_framework import (
    test,
    reverse,
)


class AttendeeTest(test.APITestCase):
    """
    test for attendee
    """

    fixtures = ['test_clubs.json', 'test_members.json']

    @unittest.mock.patch(
        'modules.club_members.views.'
        'AttendeeViewSet.permission_classes', [])
    def test_create_attendee(self):
        req_url = reverse.reverse(
            'club_members:member_attendees-list')
        req_data = {
            'name': 'Test Attendee 1',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.CREATED)
