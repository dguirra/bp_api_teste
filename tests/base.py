# -*- coding: utf-8 -*-

from flask_testing import TestCase

from ..main import create_app as real_create_app


class BaseTestCase(TestCase):

    def create_app(self):
        app = real_create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        return app
