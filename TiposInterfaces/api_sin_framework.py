import socket

def crear_respuesta(mensaje, codigo=200, tipo_contenido="text/plain"):
    respuesta = f"""HTTP/1.1 {codigo} OK\r\nContent-Type: {tipo_contenido}\r\n\r\n{mensaje}""".encode('utf-8')
    return respuesta

def manejar_solicitud(conexion):
    solicitud = conexion.recv(1024).decode('utf-8')
    if not solicitud:
        return

    lineas_solicitud = solicitud.split('\r\n')
    primera_linea = lineas_solicitud[0]
    partes_solicitud = primera_linea.split(' ')

    if len(partes_solicitud) == 3:
        metodo, ruta, protocolo = partes_solicitud

        if metodo == 'GET':
            if ruta == '/api/mensajes':
                mensajes = ["Mensaje 1", "Mensaje 2", "Mensaje 3"]
                respuesta = crear_respuesta('\n'.join(mensajes))
            elif ruta == '/api/info':
                info = "Esta es una API simple con Python socket."
                respuesta = crear_respuesta(info)
            else:
                respuesta = crear_respuesta("Ruta no encontrada", codigo=404)
        elif metodo == 'POST':
            if ruta == '/api/datos':
                respuesta = crear_respuesta("Datos recibidos correctamente", codigo=201)
            else:
                respuesta = crear_respuesta("Ruta POST no encontrada", codigo=404)
        else:
            respuesta = crear_respuesta("Método no soportado", codigo=405)
    else:
        respuesta = crear_respuesta("Solicitud inválida", codigo=400)

    conexion.sendall(respuesta)
    conexion.close()

def iniciar_servidor(host='127.0.0.1', puerto=8080):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(5)
    print(f"Servidor escuchando en {host}:{puerto}...")

    while True:
        conexion, direccion = servidor.accept()
        manejar_solicitud(conexion)

if __name__ == "__main__":
    iniciar_servidor()

# accede a los endpoints usando un navegador o curl:
# http://127.0.0.1:8080/api/mensajes
# http://127.0.0.1:8080/api/info
# curl -x post http://127.0.0.1:8080/api/datos