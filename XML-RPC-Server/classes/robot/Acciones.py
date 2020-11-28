from classes.XmlRpcServer import XmlRpcServer
from classes.Logger import Logger


class Acciones():

    def __init__(self):
        pass

    def setAnguloArticulacion(self, articulacion, sentido, angulo):
        art, sen, ang = int(articulacion), str(sentido), float(angulo)
        correct = XmlRpcServer.robot.setAnguloArt(art, sen, ang)
        if correct:
            logger = Logger(XmlRpcServer.robot)
            logger.anguloArticulacion(art, sen, ang)
            sentidoGiro = ''
            if (sentido == 'A'):
                sentidoGiro = 'antihorario'
            elif (sentido == 'H'):
                sentidoGiro = 'horario'
            return '\nLa articulación \'' + str(XmlRpcServer.robot.getNombreArt(art)) + '\' giró correctamente ' + str(float(angulo)) + '° en sentido ' + str(sentidoGiro) + ', se encuentra en ' + str(XmlRpcServer.robot.getAnguloArt(art)) + '°.\n'
        else:
            return '\nLa articulación \'' + str(XmlRpcServer.robot.getNombreArt(art)) + '\' no pudo girar correctamente, ángulo fuera de los límites. Se encuentra en ' + str(XmlRpcServer.robot.getAnguloArt(art)) + '°\n'

    def setVelocidadArticulacion(self, articulacion, velocidad):
        art, vel = int(articulacion), float(velocidad)
        correct = XmlRpcServer.robot.setVelocidadArt(art, vel)
        if correct:
            logger = Logger(XmlRpcServer.robot)
            logger.velocidadArticulacion(art, velocidad)
            return '\nSe cambió correctamente la velocidad de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(art)) + '\' a ' + str(float(velocidad)) + ' rad/s.\n'
        else:
            return '\nNo se pudo cambiar la velocidad de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(art)) + '\', límites excedidos. Se mantiene en ' + str(float(XmlRpcServer.robot.getVelocidadArt(art))) + ' rad/s.\n'

    def setEstadoEfectorFinal(self, tiempo):
        time = float(tiempo)
        XmlRpcServer.robot.setEstadoEfectorFinal(time)
        logger = Logger(XmlRpcServer.robot)
        logger.estadoEfectorFinal(time)
        return '\nSe accionó el efector final durante ' + str(time) + ' segundos.\n'

acciones = Acciones()
