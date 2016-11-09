# -*- coding: utf-8 -*-

from .blueprint import app_bp
from .models import db, Occupation
from flask import request, jsonify
from sqlalchemy import or_


@app_bp.route('/occupation', methods=["POST"])
def add_occupation():
    data = request.json
    if not data.get('description'):  # Checa se está vazio
        return jsonify({"Error": "Dados inseridos de forma incorreta ou campo vazio"}), 400  # Bad request

    if isinstance(data, dict):
        occupation = Occupation()
        occupation.description = data.get('description')
        db.session.add(occupation)

    elif isinstance(data, list):
        for row in data:
            occupation = Occupation()
            occupation.description = row.get('description')
            db.session.add(occupation)
    db.session.commit()

    return jsonify({"Status": "Success"}), 201  # Created OK


@app_bp.route('/occupation/<params>')  # Por default é GET
def get_occupation(params):
    occupation = Occupation.query.filter(or_(Occupation.id == params,
                                             Occupation.description == params)).first_or_404()
    return jsonify({"description": occupation.description, "id": occupation.id})


@app_bp.route('/occupation/<id>', methods=["DELETE"])
def delete_occupation(id):
    delete = Occupation.query.filter_by(id=id).one()
    if delete != []:
        db.session.delete(delete)
        db.session.commit()
        return jsonify({"Status": "Success"}), 200
    else:
        return jsonify({"Status": "Fail"}), 404
