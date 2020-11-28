import socket
from threading import Thread
from xmlrpc.server import SimpleXMLRPCServer
from classes.robot.Robot import Robot


class XmlRpcServer(object):

    robot = None

    def __init__(self):
        self.puerto = 8000
        self.direccion = None

        # Creacion del servidor indicando el puerto deseado
        self.server = SimpleXMLRPCServer(
            ('localhost', self.puerto), allow_none=True, logRequests=False)

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
        mensaje = 'Hola!! desde el servidor'
        return mensaje

    def do_despedir(self):
        mensaje = 'Nos vemos pibe'
        return mensaje

    def do_setAnguloArticulacion(self):
        pass

    def do_setVelocidadArticulacion(self):
        pass

    def do_setEstadoEfectorFinal(self):
        pass

    def do_getNombreRobot(self):
        return self.robot.getNombre()

    def do_getNombreArticulacion(self, articulacion):
        return self.robot.getNombreArt(int(articulacion))

    def do_getNombreEfectorFinal(self):
        return self.robot.getNombreEfectorFinal()

    def do_reporteRobot(self):
        pass

    def do_reporteAcciones(self):
        pass
