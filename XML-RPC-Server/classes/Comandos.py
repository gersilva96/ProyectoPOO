import sys
import os
from cmd import Cmd
from classes.XmlRpcServer import XmlRpcServer
from classes.Robot_RRR.ComandosRobot import ComandosR

class Comandos(Cmd):
	doc_header = 'Ayuda de comandos documentados (escriba \'help <command>\')'
	undoc_header = 'Ayuda de comandos no documentados'

	def __init__(self):
		Cmd.__init__(self)
		self.servidor = None

	def do_report(self, value):
		'''\nMuestra un reporte completo del sistema.\n'''
		print('\nMostrando reporte...\n')

	def do_mode(self,value):
		'''\nDefine el modo de funcionamiento del sistema.\''''
		options = {
			'manual': 'Modo manual',
			'automatic': 'Modo automático',
			'exit': 'Salir del comando \'mode\'',
		}
		self.printOptions(options)
		keys = []
		for key in options.keys():
			keys.append(key)
		option = ''
		while option != 'exit':
			if (option != '' and option != keys[0] and option != keys[1] and option != 'clear'):
				print('\nOpción <<'+ option +'>> no encontrada\n')
			option = input('mode >> ')
			if option.lower() == keys[0]:
				print('\nEjecutando modo manual...\n')
				rob = ComandosR()
				rob.prompt = 'Ingrese instrucción: '
				rob.cmdloop('Iniciando entrada de comandos. Intruduzca Help para ver los comandos del modo manual.')
			elif option.lower() == keys[1]:
				print('\nEjecutando modo automático...\n')
			elif option.lower() == keys[2]:
				print('\nSaliendo del comando \'mode\'...\n')
			elif option == 'clear':
				os.system('clear')
				self.printOptions(options)

	def do_xml_rpc(self, value):
		'''\nInicia o detiene el servidor XML-RPC según el valor dado (On/Off).\n'''
		options = {
			'on': 'Inicia el servidor',
			'off': 'Detiene el servidor',
			'status': 'Indica el estado actual del servidor',
			'exit': 'Salir del comando \'xml_rpc\'',
		}
		self.printOptions(options)
		keys = []
		for key in options.keys():
			keys.append(key)
		option = ''
		while option != 'exit':
			if (option != '' and option != keys[0] and option != keys[1] and option != keys[2] and option != 'clear'):
				print('\nOpción <<'+ option +'>> no encontrada\n')
			option = input('xml_rpc >> ')
			if option.lower() == keys[0]:
				print('\nIniciando servidor XML-RPC...\n')
				self.servidor = XmlRpcServer()
				print('\n\n\n\n')
			elif option.lower() == keys[1]:
				print('\nDeteniendo servidor XML-RPC...\n')
				self.servidor.shutdown()
			elif option.lower() == keys[2]:
				print('\nObteniendo estado del servidor XML-RPC...\n')
			elif option.lower() == keys[3]:
				print('\nSaliendo del comando \'xml_rpc\'...\n')
			elif option == 'clear':
				os.system('clear')
				self.printOptions(options)

	def do_clear(self, value):
		'''\nLimpia la consola.\n'''
		self.init('')

	def do_exit(self, value):
		'''\nFrena el servidor XML-RPC si está activo y finaliza el programa.\n'''
		print('')
		print('*' + '-'*70 + '*')
		print('|' + '{:^70}'.format('Programa finalizado') + '|')
		print('*' + '-'*70 + '*')
		sys.exit()

	def init(self, value):
		os.system('clear')
		print('*' + '-'*70 + '*')
		print('|' + '{:^70}'.format('Programación Orientada a Objetos 2020') + '|')
		print('|' + '{:^70}'.format('Intefaz de control servidor Robot-RRR') + '|')
		print('|' + '{:^70}'.format('') + '|')
		print('|' + '{:>70}'.format('Wieckowski, Martín - Silva, Germán') + '|')
		print('|' + '{:^70}'.format('') + '|')
		print('|' + '{:<70}'.format('Utilice el comando \'help\' para obtener ayuda del sistema.') + '|')
		print('*' + '-'*70 + '*\n')

	def printOptions(self, options):
		print('\nIngrese una de las siguientes opciones:\n')
		for key in options:
			print(key + ": " + options[key])
		print('')
