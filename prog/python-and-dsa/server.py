#!/usr/bin/env python3
"""
Tiny local HTTP server for the Python & DSA playground.

Skulpt (the in-browser Python) is fully vendored under vendor/ and needs
no special headers, so this is just plain `python -m http.server` with
two small niceties:
  - quieter logging (skips 404 spam from favicon requests)
  - a friendly startup line pointing at the URL

Usage:  python server.py          (serves on port 8000)
        python server.py 9000     (custom port)
"""
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if '404' in (args[1] if len(args) > 1 else ''):
            return
        super().log_message(fmt, *args)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"\n  Python & DSA  ->  http://localhost:{port}\n")
HTTPServer(("", port), QuietHandler).serve_forever()
