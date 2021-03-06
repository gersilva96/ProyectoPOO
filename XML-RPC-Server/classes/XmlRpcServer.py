import socket
from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from classes.robot.Robot import Robot


class XmlRpcServer(object): 
	
	rob = Robot()	
	
	def __init__(self):
		self.puerto = 8000
		

		# Creacion del servidor indicando el puerto deseado
		self.server = SimpleXMLRPCServer(('localhost', self.puerto), logRequests=False)
		# Se registra cada funcion
		self.server.register_function(self.do_saludar, 'saludar')
		self.server.register_function(self.do_despedir, 'despedir')
		self.server.register_function(self.do_RotarArticulacion1, 'RotarArticulacion1')
		self.server.register_function(self.do_RotarArticulacion2, 'RotarArticulacion2')
		self.server.register_function(self.do_RotarArticulacion3, 'RotarArticulacion3')
		self.server.register_function(self.do_ActivarEfector, 'ActivarEfector')

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

		m1 = '*' + '-'*70 + '*' + '\n'
		m2 = '|' + '{:^70}'.format('Programación Orientada a Objetos 2020') + '|' + '\n'
		#m3 = '|' + '{:^70}'.format('Intefaz de control servidor Robot-RRR') + '|' + '\n'
		m4 = '|' + '{:^70}'.format('') + '|' + '\n'
		m5 = '|' + '{:^70}'.format('Wieckowski, Martín - Silva, Germán') + '|' + '\n'
		m6 = '|' + '{:^70}'.format('') + '|' + '\n'
		m7 = '|' + '{:<70}'.format('   Bienvenido al programa Cliente    ') + '|' + '\n'
		m8 = '*' + '-'*70 + '*\n' + '\n'
		mensaje = m1+m2+m4+m5+m6+m7+m8
		return mensaje

	def do_despedir(self):
		mensaje = '\n\n******************Programa finalizado***********************\n\n'
		return mensaje

	def do_RotarArticulacion1(self, Angulo, Velocidad, Sentido):
		
		return 0

	def do_RotarArticulacion2(self, Angulo, Velocidad, Sentido):
		
		return 0

	def do_RotarArticulacion3(self, Angulo, Velocidad, Sentido):
		
		return 0

	def do_ActivarEfector(self, tiempo):
		
		return 0
