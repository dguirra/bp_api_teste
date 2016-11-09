# -*- coding: utf-8 -*-

from flask import Flask
from my_app.blueprint import app_bp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    from models.occupation import db
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/cadastro'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.db = db
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
