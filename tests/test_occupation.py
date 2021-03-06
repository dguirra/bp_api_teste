# -*- coding: utf-8 -*-

from .base import BaseTestCase
from ..my_app.models.occupation import Occupation
import json


class TestOccupation(BaseTestCase):

    def test_save_success(self):
        response = self.client.post('/occupation', data=json.dumps({'description': 'teste'}),
                                    headers={'Content-Type': 'application/json'})
        assert response.status_code == 201
        occupation_count = Occupation.query.filter_by(description='teste').count()

        assert occupation_count == 1

    def test_empty(self):
        response = self.client.post('/occupation', data=json.dumps({'description': ''}),
                                    headers={'Content-Type': 'application/json'})
        assert response.status_code == 400

    def test_without_param_description(self):
        response = self.client.post('/occupation', data=json.dumps({'': 'teste'}),
                                    headers={'Content-Type': 'application/json'})
        assert response.status_code == 400

    def test_same_occupation(self):
        self.create_occupation('sameoccupation')
        response = self.client.post('/occupation', data=json.dumps({'description': 'sameoccupation'}),
                                    headers={'Content-Type': 'application/json'})
        assert response.status_code == 409

    def test_get_occupation(self):
        self.create_occupation('teste')
        response = self.client.get(('/occupation/teste'),
                                   headers={'Content-Type': 'application/json'})
        assert response.status_code == 200


'''    def test_without_content_type(self):
        response = self.client.post('/occupation', data=json.dumps({'description': 'teste'})
'''
