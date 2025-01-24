import http
import json
import unittest.mock

from rest_framework import (
    test,
    reverse,
)


class ParticipantTest(test.APITestCase):
    """
    test for participants
    """

    fixtures = ['test_clubs.json', 'test_members.json']

    @unittest.mock.patch(
        'modules.club_participants.views.'
        'ParticipantViewSet.permission_classes', [])
    def test_create_participant(self):
        req_url = reverse.reverse(
            'club_participants:participants-list')
        req_data = {
            'name': 'Test Participant 1',
        }
        resp = self.client.post(
            req_url,
            data=json.dumps(req_data),
            content_type='application/json',
        )
        self.assertEqual(
            resp.status_code, http.HTTPStatus.CREATED)
