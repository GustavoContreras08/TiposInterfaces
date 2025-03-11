import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
resultado_suma = proxy.sumar(10, 5)
resultado_resta = proxy.restar(10, 5)
print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)