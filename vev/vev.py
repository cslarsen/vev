# -*- encoding: utf-8 -*-

"""
vev — simple HTTP server request routing

Copyright 2015 Christian Stigen Larsen

Distributed under the LGPL 2.1. You are allowed to change the license on a
particular copy to the LGPL 3.0, the GPL 2.0 or the GPL 3.0.
"""

import http.server
import urllib


class Route:
    """
    Provides a set of decorators for http.server.

    Note that all data here is stored in class variables!
    """
    routes = {}

    @staticmethod
    def bind(path):
        """Binds method to given URL path."""
        def decorator(method):
            Route.routes[path] = method
            def wrapper(func):
                return func
            return wrapper
        return decorator

    @staticmethod
    def not_found():
        """Calls method when route was not found."""
        return Route.route(None)

    @staticmethod
    def dispatch(path, *args, **kw):
        """Dispatches requests based on path."""
        not_found = Route.routes.get(None, lambda: None)
        method = Route.routes.get(path, not_found)
        result = method(*args, **kw)
        return Route.send_html(args[0], result)

    @staticmethod
    def outputs(converter):
        def decorator(method):
            def wrapper(func):
                return converter(func)
            return wrapper
        return decorator

    @staticmethod
    def send_html(obj, result, encoding="utf-8"):
        obj.send_response(200)
        obj.send_header("Content-type", "text/html; charset=%s" % encoding)
        obj.end_headers()
        obj.wfile.write(bytes(result, encoding=encoding))


class Server(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        return Route.dispatch(url.path, self)

def serve(addr_port, Class):
    addr, port = addr_port
    r = http.server.HTTPServer((addr, port), Class)
    print("Serving from %s:%s" % (addr, port))
    r.serve_forever()

def route(*args, **kw):
    return Route.bind(*args, **kw)

def send_html(*args, **kw):
    return Route.send_html(*args, **kw)
