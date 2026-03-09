#!/usr/bin/env python3
"""
Simple HTTP server for SubReader.
Run: python3 serve.py
Then open http://localhost:8080 on your phone (same Wi-Fi network).
"""
import http.server
import socket
import os

PORT = 8080

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("0.0.0.0", PORT), handler)

local_ip = get_local_ip()
print(f"\n  SubReader is running!\n")
print(f"  Local:   http://localhost:{PORT}")
print(f"  Network: http://{local_ip}:{PORT}")
print(f"\n  Open the Network URL on your iPhone (same Wi-Fi).")
print(f"  Tap Share → Add to Home Screen to install as an app.\n")
print(f"  Press Ctrl+C to stop.\n")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    httpd.server_close()
