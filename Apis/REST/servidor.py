import http.server
import json
import os
class SimpleHandler(http.server.BaseHTTPRequestHandler):
    productos = [
        {'id': 1, 'nombre': 'Laptop', 'precio': 1200},
        {'id': 2, 'nombre': 'Mouse', 'precio': 25}
    ]
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/productos':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.productos).encode())
        elif self.path.startswith('/productos/'):
            try:
                id = int(self.path.split('/')[-1])
                producto = next((p for p in self.productos if p['id'] == id), None)
                if producto:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(producto).encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'mensaje': 'Producto no encontrado'}).encode())
            except ValueError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'mensaje': 'ID inválido'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    def do_POST(self):
        if self.path == '/productos':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                nuevo_producto = json.loads(post_data.decode())
                self.productos.append(nuevo_producto)
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(nuevo_producto).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'mensaje': 'Datos inválidos'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
if __name__ == '__main__':
    with http.server.HTTPServer(('localhost', 8000), SimpleHandler) as httpd:
        print('Servidor escuchando en el puerto 8000')
        httpd.serve_forever()