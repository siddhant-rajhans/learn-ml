#!/usr/bin/env python3
"""
Pyodide-compatible local server.
Adds Cross-Origin-Opener-Policy + Cross-Origin-Embedder-Policy headers
so the browser enables SharedArrayBuffer — required for Pyodide's fast path.

Usage:  python server.py          (serves on port 8000)
        python server.py 9000     (custom port)
"""
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CoopCoepHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy",   "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "credentialless")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Cleaner output — skip favicon 404 spam
        if '404' in (args[1] if len(args) > 1 else ''):
            return
        super().log_message(fmt, *args)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"\n  Python & DSA  →  http://localhost:{port}\n")
HTTPServer(("", port), CoopCoepHandler).serve_forever()
