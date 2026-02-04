import http.server
import socketserver

PORT = 8080 
Handler = http.server.SimpleHTTPRequestHandler

print(f"[*] Сервис запущен на порту {PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
