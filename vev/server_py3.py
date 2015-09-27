import http.server
import urllib.parse

class BaseServer(http.server.BaseHTTPRequestHandler):
    pass

HTTPServer = http.server.HTTPServer
urllib_urlparse = urllib.parse.urlparse
