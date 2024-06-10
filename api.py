from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8501

Handler = SimpleHTTPRequestHandler

httpd = TCPServer(("127.0.0.1", PORT), Handler)

print(f"Serving on port {PORT}")
httpd.serve_forever()
