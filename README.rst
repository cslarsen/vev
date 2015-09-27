vev — simple HTTP server request routing
========================================

An *extremely* simple web routing scheme based on Python 3's ``http.server``
module, vev makes it easy to quickly create simple web servers.  At this point,
it's basically just an experiment.

"Vev" is the Norwegian word for "web".

Example
=======

::

    import vev

    class HelloWorld(vev.Server):
        @vev.route("/")
        def index(self):
            return "<html><body><a href='/foo'>Foo</a></body></html>"

        @vev.route("/foo")
        def foo(self):
            return "<html><body><a href='/'>Start</a></body></html>"

    if __name__ == "__main__":
        vev.serve(("0.0.0.0", 8080), HelloWorld)

License
-------
Copyright 2015 Christian Stigen Larsen

Distributed under the LGPL 2.1. You are allowed to change the license on a
particular copy to the LGPL 3.0, the GPL 2.0 or the GPL 3.0.
