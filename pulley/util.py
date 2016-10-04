from flask.views import MethodView
from flask import request


class PulleyMethodView(MethodView):
    """A subclass of :class: `flask.views.MethodView` which allows
     for decorating view functions at the method level in addition
     to the standard decorator assignment.

    Example:
        decorators = [user_required] # applies to all methods
        _decorators = {'post':[admin_required, format_results]} # applies to only post method


    """
    _decorators = {}

    # Taken from flask
    def dispatch_request(self, *args, **kwargs):
        meth = getattr(self, request.method.lower(), None)
        # If the request method is HEAD and we don't have a handler for it
        # retry with GET.
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        method_decorators = self._decorators.get(request.method.lower())
        assert isinstance(method_decorators, list), '_decorators requires an iterable of type list'

        if method_decorators:
            for decorator in method_decorators:
                meth = decorator(meth)
            return meth(*args, **kwargs)
        return meth(*args, **kwargs)

