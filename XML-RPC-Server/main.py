import os
from classes.PanelDeControl import PanelDeControl
from classes.Utils import utils
from classes.XmlRpcServer import XmlRpcServer
from classes.robot.Robot import Robot


# Creo el archivo de logs dejándolo vacío al principio
with open('logs/log.txt', '+w') as f:
  pass

# Inicializo la CLI
utils.init()
nombreRobot = input('Ingrese el nombre del robot: ')
XmlRpcServer.robot = Robot(nombreRobot)
print('')
cli = PanelDeControl()
cli.prompt = '>> '
cli.cmdloop()
