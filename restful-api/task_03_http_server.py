#!/usr/bin/python3
'''
Handle different types of HTTP requests
'''
import json
import http.server


class http_request(http.server.BaseHTTPRequestHandler):
    """
    Classe qui gère les requêtes HTTP
    """
    def do_GET(self):
        # Check the requested path
        if self.path == "/":
            # Serve the simple text message
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == "/data":
            # Serve JSON data
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Example dataset
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convert dictionary to JSON and send it
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(json_data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Handle undefined endpoints with 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


# Numéro du port à utiliser (8000)
PORT = 8000

# Configurer et démarrer le serveur HTTP
with http.server.HTTPServer(("", PORT), http_request) as httpd:
    httpd.serve_forever()
