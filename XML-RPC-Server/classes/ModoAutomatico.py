from classes.XmlRpcServer import XmlRpcServer
from classes.robot.Acciones import acciones


def modoAutomatico():
    print('\nEjecutando el modo automático...\n')

    print('\nIntentando mover la articulación \'' + str(XmlRpcServer.robot.getNombreArt(0)) + '\', 20° en sentido antihorario...')
    intento = acciones.setAnguloArticulacion(0, 'A', 20)
    print(intento)

    print('\nIntentando mover la articulación \'' + str(XmlRpcServer.robot.getNombreArt(1)) + '\', 15° en sentido antihorario...')
    intento = acciones.setAnguloArticulacion(1, 'A', 15)
    print(intento)

    print('\nIntentando mover la articulación \'' + str(XmlRpcServer.robot.getNombreArt(2)) + '\', 5° en sentido horario...')
    intento = acciones.setAnguloArticulacion(2, 'H', 5)
    print(intento)

    print('\nIntentando cambiar la velocidad de la articulación \'' + str(XmlRpcServer.robot.getNombreArt(2)) + '\', a 6.5 rad/s...')
    intento = acciones.setVelocidadArticulacion(2, 6.5)
    print(intento)

    print('\nIntentando mover la articulación \'' + str(XmlRpcServer.robot.getNombreArt(2)) + '\', 90° en sentido antihorario...')
    intento = acciones.setAnguloArticulacion(2, 'A', 90)
    print(intento)

    print('\nIntentando accionar el efector final 5 segundos...')
    intento = acciones.setEstadoEfectorFinal(5)
    print(intento)

    print('\n*************Modo automático finalizado***************\n')
