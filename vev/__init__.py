# -*- encoding: utf-8 -*-

"""
vev — simple HTTP server request routing

Copyright 2015 Christian Stigen Larsen

Distributed under the LGPL 2.1. You are allowed to change the license on a
particular copy to the LGPL 3.0, the GPL 2.0 or the GPL 3.0.
"""

from .vev import (
    Route,
    Server,
    route,
    send_html,
    serve,
)

__all__ = [
    "Route",
    "Server",
    "route",
    "send_html",
    "serve",
]

__author__ = "Christian Stigen Larsen"
__copyright__ = "Copyright 2015, Christian Stigen Larsen"
__credits__ = ["Christian Stigen Larsen"]
__email__ = "csl@csl.name"
__license__ = "LGPL"
__maintainer__ = "Christian Stigen Larsen"
__status__ = "Prototype"
__version__ = "0.5.0"
