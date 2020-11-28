class Reporte():

    def __init__(self, robot):
        self.robot = robot

    def reporteRobot(self):
        modoRobot = 'manual'
        if self.robot.getModoAutomatico():
            modoRobot = 'automático'
        estadoEfectorFinal = ''
        if self.robot.getEstadoEfectorFinal():
            estadoEfectorFinal = 'sujetando'
        else:
            estadoEfectorFinal = 'liberado'
        return f'''
    *{'-'*40}*

    Datos del robot

    # ID: {self.robot.getId()}
    # Nombre: {self.robot.getNombre()}
    # Versión: {self.robot.getVersion()}
    # Modo: {modoRobot}
    # Cantidad de articulaciones: {self.robot.getCantidadArticulaciones()}
    # Cantidad de efectores finales: 1

    *{'-'*40}*
    {self.printDatosArticulacion(0)}
    *{'-'*40}*
    {self.printDatosArticulacion(1)}
    *{'-'*40}*
    {self.printDatosArticulacion(2)}
    *{'-'*40}*

    Datos del efector final

    # ID: {self.robot.getIdEfectorFinal()}
    # Nombre: {self.robot.getNombreEfectorFinal()}
    # Estado: {estadoEfectorFinal}

    *{'-'*40}*
    '''

    def printDatosArticulacion(self, art):
        return f'''
    Datos de la {str(art+1)}° articulación

    # ID: {self.robot.getIdArt(art)}
    # Nombre: {self.robot.getNombreArt(art)}
    # Posición actual: {self.robot.getAnguloArt(art)}°
    # Velocidad: {self.robot.getVelocidadArt(art)} rad/s
    '''

    def reporteAcciones(self):
        report = '\n'
        with open('logs/log.txt', 'r') as f:
            report += f.read()
        return report
