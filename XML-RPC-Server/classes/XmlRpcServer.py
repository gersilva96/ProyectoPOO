import socket
from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer

class XmlRpcServer(object):
	def __init__(self):
		self.puerto = 8000

		# Creacion del servidor indicando el puerto deseado
		self.server = SimpleXMLRPCServer(('localhost', self.puerto), logRequests=False)

		# Se registra cada funcion
		self.server.register_function(self.do_saludar, 'saludar')
		self.server.register_function(self.do_despedir, 'despedir')
		self.server.register_function(self.do_sumar, 'sumar')
		self.server.register_function(self.do_restar, 'restar')
		self.server.register_function(self.do_multiplicar, 'multiplicar')
		self.server.register_function(self.do_dividir, 'dividir')

		# Se lanza el servidor
		self.thread = Thread(target=self.run_server)
		self.thread.start()
		print('Servidor XML-RPC iniciado en [' + str(self.server.server_address[0]) + '], puerto [' + str(self.server.server_address[1]) + ']')

	def run_server(self):
		self.server.serve_forever()

	def shutdown(self):
		self.server.shutdown()
		self.thread.join()

	def do_saludar(self):
		mensaje = 'Hola!! desde el servidor'
		return mensaje

	def do_despedir(self):
		mensaje = 'Nos vemos pibe'
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
