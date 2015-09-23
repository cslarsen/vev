# -*- encoding: utf-8 -*-

"""
vev — simple HTTP server request routing

Copyright 2015 Christian Stigen Larsen

Distributed under the LGPL 2.1. You are allowed to change the license on a
particular copy to the LGPL 3.0, the GPL 2.0 or the GPL 3.0.
"""

class Vev:
    """
    Provides a set of decorators for http.server.

    Note that all data here is stored in class variables!
    """
    routes = {}

    @staticmethod
    def route(path):
        """Binds method to given URL path."""
        def decorator(method):
            Vev.routes[path] = method
            def wrapper(func):
                return func
            return wrapper
        return decorator

    @staticmethod
    def not_found():
        """Calls method when route was not found."""
        return Vev.route(None)

    @staticmethod
    def dispatch(path, *args, **kw):
        """Dispatches requests based on path."""
        not_found = Vev.routes.get(None, lambda: None)
        method = Vev.routes.get(path, not_found)
        result = method(*args, **kw)
        return result

    @staticmethod
    def outputs(converter):
        def decorator(method):
            def wrapper(func):
                return converter(func)
            return wrapper
        return decorator

    @staticmethod
    def send_html(obj, result):
        obj.send_response(200)
        obj.send_header("Content-type", "text/html; charset=utf-8")
        obj.end_headers()
        obj.wfile.write(bytes(result, encoding="utf-8"))

    @staticmethod
    def return_html():
        return Vev.outputs(Vev.send_html)
