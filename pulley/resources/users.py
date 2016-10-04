# -*- coding: utf-8 -*-
"""
    pulley.resources.users
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Andrew Bednar.
"""
from flask.views import MethodView
from flask import jsonify, request

users = []


class UsersCollection(MethodView):
    """Users collection resource implemented using :class: MethodView"""
    decorators = []

    def get(self):
        return jsonify(users), 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return jsonify({'message': 'No input data provided'}), 400
        users.append(json_data)
        return jsonify(users), 201
