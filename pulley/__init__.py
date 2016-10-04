# -*- coding: utf-8 -*-
"""
    pulley
    ~~~~~~

    :copyright: (c) 2016 by Andrew Bednar.
"""
from flask import Flask
from .config import config_by_name
from .resources.users import UsersCollection


def create_app(config_name):
    """App creation factory"""
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config_by_name['dev'])

    # routing
    app.add_url_rule('/users', endpoint='users', view_func=UsersCollection.as_view('users'))

    return app
