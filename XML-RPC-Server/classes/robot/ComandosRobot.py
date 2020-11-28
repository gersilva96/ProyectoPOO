import os
import time
import sys
from cmd import Cmd
from classes.robot.Robot import Robot
from classes.Utils import utils
from classes.XmlRpcServer import XmlRpcServer
from classes.robot.Acciones import acciones


class ComandosRobot():

    def __init__(self):
        pass

    def articulaciones(self):
        options = {
            '1': 'Modificar valores de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(0)) + '\'',
            '2': 'Modificar valores de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(1)) + '\'',
            '3': 'Modificar valores de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(2)) + '\'',
            'exit': 'Salir del comando \'mode >> manual >> art\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(str(key))
        option = ''
        while option != 'exit':
            option = str(input('mode >> manual >> art >> ').lower())
            if option == keys[0]:
                self.articulacion(0)
            elif option == keys[1]:
                self.articulacion(1)
            elif option == keys[2]:
                self.articulacion(2)
            elif option == keys[3]:
                print('\nSaliendo del comando \'mode >> manual >> art\'...\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')

    def articulacion(self, art):
        options = {
            'ang': 'Rotar la articulación',
            'vel': 'Modificar la velocidad de los movimientos',
            'exit': 'Salir del comando \'mode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + '\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        option = ''
        while option != 'exit':
            option = input('mode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + ' >> ').lower()
            if option == keys[0]:
                sentido = ''
                while (sentido != 'H' and sentido != 'A'):
                    sentido = input('\nmode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + ' >> ang >> Ingrese el sentido (H: horario, A: antihorario): ').upper()
                angulo = float(input('\nmode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + ' >> ang >> Ingrese el ángulo (en grados): '))
                result = acciones.setAnguloArticulacion(art, sentido, angulo)
                print(result)
            elif option == keys[1]:
                velocidad = float(input('\nmode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + ' >> vel >> Ingrese la velocidad a setear: '))
                result = acciones.setVelocidadArticulacion(art, velocidad)
                print(result)
            elif option == keys[2]:
                print('\nSaliendo del comando \'mode >> manual >> art >> ' + str(XmlRpcServer.robot.getNombreArt(art)) + '\'...\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')

    def efectorFinal(self):
        options = {
            'set': 'Setear el efector final',
            'exit': 'Salir del comando \'mode >> manual >> eff\'',
        }
        utils.printOptions(options)
        keys = []
        for key in options.keys():
            keys.append(key)
        option = ''
        while option != 'exit':
            option = input('mode >> manual >> eff >> ').lower()
            if option == keys[0]:
                time = 0
                while (time <= 0):
                    time = float(input('mode >> manual >> eff >> Ingrese el tiempo (en segundos): '))
                result = acciones.setEstadoEfectorFinal(time)
                print(result)
            elif option == keys[1]:
                print('\nSaliendo del comando \'mode >> manual >> eff\'...\n')
            elif option == 'help':
                utils.printOptions(options)
            elif option == 'clear':
                os.system('clear')
                utils.init()
                utils.printOptions(options)
            else:
                print('\nOpción <<' + option + '>> no encontrada\n')
