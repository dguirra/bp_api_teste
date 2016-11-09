# -*- coding: utf-8 -*-
from models import db, ModelMixin


class Occupation(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)
