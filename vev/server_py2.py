import BaseHTTPServer
import urlparse

class BaseServer(BaseHTTPServer.BaseHTTPRequestHandler):
    pass

HTTPServer = BaseHTTPServer.HTTPServer
urllib_urlparse = urlparse.urlparse
