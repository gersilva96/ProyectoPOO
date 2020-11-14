import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket
from classes.Comandos import Comandos

class XmlRpcServer(object):
	def __init__(self):
		# Creacion del servidor indicando el puerto deseado
		self.server = SimpleXMLRPCServer(("localhost", 8000))

		# Se registra cada funcion
		self.server.register_function(self.do_saludar, 'saludar')
		self.server.register_function(self.do_comandos, 'comandos')
		self.server.register_function(self.do_sumar, 'sumar')

		# Se lanza el servidor
		self.thread = Thread(target=self.run_server)
		self.thread.start()
		print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))

	def run_server(self):
		self.server.serve_forever()

	def shutdown(self):
		self.server.shutdown()
		self.thread.join()

	def do_saludar(self):
		mensaje = "Hola!! desde el servidor"
		return mensaje

	def do_sumar(self, num1, num2):
		suma = num1 + num2
		return suma

	def do_comandos(self):
		mensaje = Comandos().cmdloop()
		return mensaje
