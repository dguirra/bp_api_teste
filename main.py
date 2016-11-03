# -*- coding: utf-8 -*-

from flask import Flask
from my_app.blueprint import app_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
