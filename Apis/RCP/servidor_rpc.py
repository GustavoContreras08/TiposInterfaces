from xmlrpc.server import SimpleXMLRPCServer
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC escuchando en el puerto 8000...")
server.register_function(sumar, "sumar")
server.register_function(restar, "restar")
server.serve_forever()