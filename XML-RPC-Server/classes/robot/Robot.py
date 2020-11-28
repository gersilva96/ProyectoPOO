import uuid
from classes.robot.Articulacion import Articulacion
from classes.robot.EfectorFinal import EfectorFinal


class Robot():

    def __init__(self, nombre):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.version = 'v1.0.0'
        self.automatico = False
        self.articulaciones = []
        self.articulaciones.append(Articulacion(uuid.uuid4(), 'Base', 0.0, 360.0, 10.0))
        self.articulaciones.append(Articulacion(uuid.uuid4(), 'Base-Codo', 45.0, 90.0, 10.0))
        self.articulaciones.append(Articulacion(uuid.uuid4(), 'Codo-EfectorFinal', 0.0, 60.0, 10.0))
        self.efectorFinal = EfectorFinal(uuid.uuid4(), 'Pinza')

    # Getters y Setters del robot
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getVersion(self):
        return self.version

    def getModoAutomatico(self):
        return self.automatico

    def getCantidadArticulaciones(self):
        return len(self.articulaciones)

    def setModoAutomatico(self, boolean):
        self.automatico = boolean

    # Getters y Setters de las articulaciones
    def getIdArt(self, articulacion):
        return self.articulaciones[articulacion].getId()

    def getNombreArt(self, articulacion):
        return self.articulaciones[articulacion].getNombre()

    def getAnguloArt(self, articulacion):
        return self.articulaciones[articulacion].getAngulo()

    def getVelocidadArt(self, articulacion):
        return self.articulaciones[articulacion].getVelocidad()

    def setAnguloArt(self, articulacion, sentido, angulo):
        return self.articulaciones[articulacion].setAngulo(sentido, angulo)

    def setVelocidadArt(self, articulacion, velocidad):
        return self.articulaciones[articulacion].setVelocidad(velocidad)

    # Getters y Setters del efector final
    def getIdEfectorFinal(self):
        return self.efectorFinal.getId()

    def getNombreEfectorFinal(self):
        return self.efectorFinal.getNombre()

    def getEstadoEfectorFinal(self):
        return self.efectorFinal.getEstado()

    def setEstadoEfectorFinal(self, tiempo):
        self.efectorFinal.setEstado(tiempo)
