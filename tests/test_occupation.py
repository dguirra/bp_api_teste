# -*- coding: utf-8 -*-

from .base import BaseTestCase
from ..my_app.models import Occupation
import json


class TestOccupation(BaseTestCase):

    def test_save_success(self):
        response = self.client.post('/occupation', data=json.dumps({'description': 'teste'}),
                                    headers={'Content-Type': 'application/json'})
        assert response.status_code == 201
        occupation_count = Occupation.query.filter_by(description='teste').count()

        assert occupation_count == 1

    def test_empty

    def test_occupation_same_name

    def test_without_content_type (json)

    




