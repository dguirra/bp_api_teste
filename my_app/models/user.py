# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth = db.Column(db.Date)
    id_occupation = db.Column(db.Integer, db.ForeignKey('occupation.id'))
