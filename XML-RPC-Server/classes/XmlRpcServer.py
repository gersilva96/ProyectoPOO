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
		self.server.register_function(self.do_despedir, 'despedir')
		self.server.register_function(self.do_comandos, 'comandos')
		self.server.register_function(self.do_sumar, 'sumar')
		self.server.register_function(self.do_restar, 'restar')
		self.server.register_function(self.do_multiplicar, 'multiplicar')
		self.server.register_function(self.do_dividir, 'dividir')

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

	def do_despedir(self):
		mensaje = "Nos vemos pibe"
		return mensaje

	def do_sumar(self, num1, num2):
		suma = num1 + num2
		return suma

	def do_restar(self, num1, num2):
		resta = num1 - num2
		return resta

	def do_multiplicar(self, num1, num2):
		multiplicacion = num1 * num2
		return multiplicacion

	def do_dividir(self, num1, num2):
		if num2 == 0:
			return 'Cómo vas a dividir por cero?'
		division = num1 / num2
		return division

	def do_comandos(self):
		mensaje = Comandos().cmdloop()
		return mensaje
