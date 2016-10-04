# -*- coding: utf-8 -*-
"""
    tests.test_units
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Andrew Bednar.
"""
from pulley.util import PulleyMethodView
from unittest.mock import Mock


def test_pulley_methodview_decoration(app):
    func = Mock()

    class TestPulleyMethodView(PulleyMethodView):
        _decorators = {'get': [func]}

        def get(self):
            return 'response'

    ctx = app.test_request_context(path='/testpath', method='GET')
    ctx.push()
    try:
        TestPulleyMethodView().dispatch_request()
    finally:
        ctx.pop()
    assert func.called
