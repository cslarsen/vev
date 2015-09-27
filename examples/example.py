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
