#!/usr/bin/env python3
"""
A simple HTTP server implementing a basic API
"""
import http.server
import socketserver
import json
import socket


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handler for our simple API server"""

    def do_GET(self): 
        """Handle GET requests"""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())

PORT = 8000

with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
