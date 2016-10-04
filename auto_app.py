# -*- coding: utf-8 -*-
"""
    auto_app
    ~~~~~~~~

    :copyright: (c) 2016 by Andrew Bednar.

    :note: Use `$env:FLASK_APP = '.\auto_app.py'` to set the click
    FLASK_APP in Powershell
"""

from pulley import create_app

app = create_app('dev')
