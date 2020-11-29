import socket
from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from classes.robot.Robot import Robot
from classes.Logger import Logger
from classes.Reporte import Reporte


class XmlRpcServer(object):

    robot = None

    def __init__(self):
        self.puerto = 8000
        self.direccion = None

        # Creacion del servidor indicando el puerto deseado
        self.server = SimpleXMLRPCServer(('localhost', self.puerto), allow_none = True, logRequests = False)

        # Se registra cada funcion
        self.server.register_function(self.do_saludar, 'saludar')
        self.server.register_function(self.do_despedir, 'despedir')
        self.server.register_function(self.do_setAnguloArticulacion, 'setAnguloArticulacion')
        self.server.register_function(self.do_setVelocidadArticulacion, 'setVelocidadArticulacion')
        self.server.register_function(self.do_setEstadoEfectorFinal, 'setEstadoEfectorFinal')
        self.server.register_function(self.do_getNombreRobot, 'getNombreRobot')
        self.server.register_function(self.do_getNombreArticulacion, 'getNombreArticulacion')
        self.server.register_function(self.do_getNombreEfectorFinal, 'getNombreEfectorFinal')
        self.server.register_function(self.do_reporteRobot, 'reporteRobot')
        self.server.register_function(self.do_reporteAcciones, 'reporteAcciones')

        # Se lanza el servidor
        self.thread = Thread(target=self.run_server)
        self.thread.start()
        self.direccion = self.server.server_address[0]
        print('Servidor XML-RPC iniciado en [' + str(self.server.server_address[0]) + ':' + str(self.server.server_address[1]) + ']\n')

    def run_server(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.thread.join()
        self.server = None

    def do_saludar(self):
        m1 = '*' + '-'*70 + '*' + '\n'
        m2 = '|' + '{:^70}'.format('Programación Orientada a Objetos 2020') + '|' + '\n'
        m4 = '|' + '{:^70}'.format('') + '|' + '\n'
        m5 = '|' + '{:^70}'.format('Wieckowski, Martín - Silva, Germán') + '|' + '\n'
        m6 = '|' + '{:^70}'.format('') + '|' + '\n'
        m7 = '|' + '{:<70}'.format('   Bienvenido al programa Cliente    ') + '|' + '\n'
        m8 = '*' + '-'*70 + '*\n' + '\n'
        mensaje = m1+m2+m4+m5+m6+m7+m8
        return mensaje

    def do_despedir(self):
        return '¡¡Hasta luego!!'

    def do_setAnguloArticulacion(self, articulacion, sentido, angulo):
        art, sen, ang = int(articulacion), str(sentido), float(angulo)
        correct = self.robot.setAnguloArt(art, sen, ang)
        if correct:
            logger = Logger(self.robot)
            logger.anguloArticulacion(art, sen, ang)
            sentidoGiro = ''
            if (sentido == 'A'):
                sentidoGiro = 'antihorario'
            elif (sentido == 'H'):
                sentidoGiro = 'horario'
            return '\nLa articulación \'' + str(self.robot.getNombreArt(art)) + '\' giró correctamente ' + str(float(angulo)) + '° en sentido ' + str(sentidoGiro) + ', se encuentra en ' + str(self.robot.getAnguloArt(art)) + '°.\n'
        else:
            return '\nLa articulación \'' + str(self.robot.getNombreArt(art)) + '\' no pudo girar correctamente, ángulo fuera de los límites. Se encuentra en ' + str(self.robot.getAnguloArt(art)) + '°\n'

    def do_setVelocidadArticulacion(self, articulacion, velocidad):
        art, vel = int(articulacion), float(velocidad)
        correct = self.robot.setVelocidadArt(art, vel)
        if correct:
            logger = Logger(self.robot)
            logger.velocidadArticulacion(art, velocidad)
            return '\nSe cambió correctamente la velocidad de la articulación \'' + str(self.robot.getNombreArt(art)) + '\' a ' + str(float(velocidad)) + ' rad/s.\n'
        else:
            return '\nNo se pudo cambiar la velocidad de la articulación \'' + str(self.robot.getNombreArt(art)) + '\', límites excedidos. Se mantiene en ' + str(float(self.robot.getVelocidadArt(art))) + ' rad/s.\n'

    def do_setEstadoEfectorFinal(self, tiempo):
        time = float(tiempo)
        self.robot.setEstadoEfectorFinal(time)
        logger = Logger(self.robot)
        logger.estadoEfectorFinal(time)
        return '\nSe accionó el efector final durante ' + str(time) + ' segundos.\n'

    def do_getNombreRobot(self):
        return self.robot.getNombre()

    def do_getNombreArticulacion(self, articulacion):
        return self.robot.getNombreArt(int(articulacion))

    def do_getNombreEfectorFinal(self):
        return self.robot.getNombreEfectorFinal()

    def do_reporteRobot(self):
        reporte = Reporte(self.robot)
        return reporte.reporteRobot()

    def do_reporteAcciones(self):
        reporte = Reporte(self.robot)
        return reporte.reporteAcciones()
