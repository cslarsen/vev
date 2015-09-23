vev — simple HTTP server request routing
========================================

An *extremely* simple web routing scheme.  It's currently just a personal
experiment.

"Vev" is the Norwegian word for "web".

Example
=======

::

    from vev import Vev
    import http.server
    import urllib.parse

    class HelloWorld(http.server.BaseHTTPRequestHandler):
        def __init__(self, *args, **kw):
            super().__init__(*args, **kw)

        def do_GET(self):
            self.log_message("GET %s", self.path)
            url = urllib.parse.urlparse(self.path)
            return Vev.dispatch(url.path, self)

        @Vev.route("/")
        def index(self):
            html = '<html><body>Go to <a href="/foo">foo</a>'
            return Vev.send_html(self, html)

        @Vev.not_found()
        def not_found(self):
            self.send_error(404, "Not found: %s" % self.path)

        @Vev.route("/foo")
        def foo(self):
            html = '<html><body>Go <a href="/">back</a></body></html>'
            return Vev.send_html(self, html)

    if __name__ == "__main__":
        try:
            addr = ("0.0.0.0", 8080)
            r = http.server.HTTPServer(addr, HelloWorld)
            print("Serving from %s:%s" % (addr[0], addr[1]))
            r.serve_forever()
        except KeyboardInterrupt:
            r.server_close()


License
-------
Copyright 2015 Christian Stigen Larsen

Distributed under the LGPL 2.1. You are allowed to change the license on a
particular copy to the LGPL 3.0, the GPL 2.0 or the GPL 3.0.
