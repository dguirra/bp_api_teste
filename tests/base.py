# -*- coding: utf-8 -*-

from flask_testing import TestCase

from ..app import create_app as real_create_app


class BaseTestCase(TestCase):

    def create_app(self):
        app = real_create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        return app
