from http.server import BaseHTTPRequestHandler
import json
import random
from urllib.parse import urlparse, parse_qs

RTO_DATA = {
    "BR01": "Patna",
    "WB26": "West Bengal",
    "DL01": "Delhi",
    "MH12": "Pune",
    "UP32": "Lucknow"
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        rc = query.get("rc", [""])[0].upper()

        if not rc:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps({"error": "RC number required"}).encode())
            return

        response = {
            "status": "success",
            "vehicle_number": rc,
            "owner_name": random.choice(["Ravi Kumar", "Amit Singh", "Abhishek Kumar"]),
            "vehicle_model": random.choice(["Activa", "i20", "Swift"]),
            "fuel_type": random.choice(["Petrol", "Diesel"]),
            "rto": RTO_DATA.get(rc[:4], "Unknown")
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
