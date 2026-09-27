from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HealthTrackerAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/health":
            response = {
                "status": "healthy",
                "service": "HealthTracker API"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("localhost", 8000), HealthTrackerAPI)

print("HealthTracker API running on http://localhost:8000")

server.serve_forever()