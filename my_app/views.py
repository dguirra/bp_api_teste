# -*- coding: utf-8 -*-

from .blueprint import app_bp
from .models import db, Occupation
from flask import request, jsonify

'''@app_bp.route('/')
def index():
    return '<h1>Hello, world!</h1>'
'''


@app_bp.route('/')
def test():
    return ('OK'), 200


@app_bp.route('/occupation', methods=["POST"])
def add_occupation():
    data = request.json
    if isinstance(data, dict):
        occupation = Occupation()
        occupation.description = data.get('description')
        db.session.add(occupation)

    elif isinstance(data, list):
        for row in data:
            occupation = Occupation()
            occupation.description = row.get('description')
            db.session.add(occupation)
    else:
        return jsonify({"Error": "Dados inseridos de forma incorreta"}), 400  # Bad request
    db.session.commit()

    return jsonify({"Status": "Success"}), 201  # Created OK
