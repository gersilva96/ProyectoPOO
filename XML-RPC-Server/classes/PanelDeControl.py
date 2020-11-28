import sys
import os
from cmd import Cmd
from classes.XmlRpcServer import XmlRpcServer
from classes.robot.Robot import Robot
from classes.robot.ComandosRobot import ComandosRobot
from classes.Reporte import Reporte
from classes.Utils import utils
from classes.ModoAutomatico import modoAutomatico


class PanelDeControl(Cmd):
    doc_header = 'Ayuda de comandos documentados (escriba \'help <command>\')'
    undoc_header = 'Ayuda de comandos no documentados'

    def __init__(self):
        Cmd.__init__(self)
        self.server = None

    def default(self, args):
        print('\nOpción <<' + args + '>> no encontrada\n')

    def do_report(self, value):
        '''\nMuestra un reporte completo del sistema.\n'''
        options = {
            'robot': 'Reporte del robot',
            'actions': 'Reporte de las acciones realizadas',
            'exit': 'Salir del comando \'report\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        reporte = Reporte(XmlRpcServer.robot)
        option = ''
        while option != 'exit':
            option = input('report >> ').lower()
            if option == keys[0]:
                print(reporte.reporteRobot())
            elif option == keys[1]:
                print(reporte.reporteAcciones())
            elif option == keys[2]:
                print('\nSaliendo del comando \'report\'\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')

    def do_mode(self, value):
        '''\nDefine el modo de funcionamiento del sistema.\n'''
        options = {
            'manual': 'Modo manual',
            'automatic': 'Modo automático',
            'exit': 'Salir del comando \'mode\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        option = ''
        while option != 'exit':
            option = input('mode >> ').lower()
            if option == keys[0]:
                self.comandosRobot()
            elif option == keys[1]:
                modoAutomatico()
            elif option == keys[2]:
                print('\nSaliendo del comando \'mode\'...\n')
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')

    def do_xml_rpc(self, value):
        '''\nInicia o detiene el servidor XML-RPC según el valor dado (On/Off).\n'''
        options = {
            'on': 'Inicia el servidor',
            'off': 'Detiene el servidor',
            'status': 'Indica el estado actual del servidor',
            'exit': 'Salir del comando \'xml_rpc\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        option = ''
        while option != 'exit':
            option = input('xml_rpc >> ').lower()
            if option == keys[0]:
                if self.server == None:
                    print('\nIniciando servidor XML-RPC...')
                    self.server = XmlRpcServer()
                else:
                    print('\nEl servidor ya se encuentra iniciado en [' + str(
                        self.server.direccion) + ':' + str(self.server.puerto) + '].\n')
            elif option == keys[1]:
                if self.server == None:
                    print('\nEl servidor no está corriendo.\n')
                else:
                    print('\nDeteniendo servidor XML-RPC...\n')
                    self.server.shutdown()
                    self.server = None
            elif option == keys[2]:
                if self.server == None:
                    print('\nEstado del servidor: detenido.\n')
                else:
                    print('\nEstado del servidor: iniciado en [' + str(
                        self.server.direccion) + ':' + str(self.server.puerto) + '].\n')
            elif option == keys[3]:
                print('\nSaliendo del comando \'xml_rpc\'...\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')

    def do_clear(self, value):
        '''\nLimpia la consola.\n'''
        utils.init()

    def do_exit(self, value):
        '''\nDetiene el servidor XML-RPC si está activo y finaliza el programa.\n'''
        print('')
        print('*' + '-'*70 + '*')
        print('|' + '{:^70}'.format('Programa finalizado') + '|')
        print('*' + '-'*70 + '*')
        sys.exit()

    def comandosRobot(self):
        comandosRobot = ComandosRobot()
        options = {
            'art': 'Modificar estado de alguna articulación',
            'eff': 'Modificar estado del efector final',
            'exit': 'Salir del comando \'mode >>manual\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        option = ''
        while option != 'exit':
            option = input('mode >> manual >> ').lower()
            if option == keys[0]:
                comandosRobot.articulaciones()
            elif option == keys[1]:
                comandosRobot.efectorFinal()
            elif option == keys[2]:
                print('\nSaliendo del comando \'mode >> manual\'\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')
