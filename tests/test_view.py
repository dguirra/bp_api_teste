# -*- coding: utf-8 -*-

from .base import BaseTestCase


class TestMyApp(BaseTestCase):

    def test_request(self):
        response = self.client.get('/')
        assert response.status_code == 200
