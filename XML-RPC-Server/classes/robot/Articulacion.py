import time
import math


class Articulacion():

    def __init__(self, id, nombre, anguloMinimo, anguloMaximo, velocidadMaxima):
        self.id = id
        self.nombre = nombre
        self.angulo = 0.0
        self.anguloMinimo = anguloMinimo
        self.anguloMaximo = anguloMaximo
        self.velocidad = 0.2
        self.velocidadMinima = 0.01
        self.velocidadMaxima = velocidadMaxima

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAngulo(self):
        return self.angulo

    def getVelocidad(self):
        return self.velocidad

    def setAngulo(self, sentido, angulo):
        sen, ang = str(sentido).upper(), float(angulo)
        if (sen == 'H'):
            sePuedeGirar = (self.angulo - ang) >= self.anguloMinimo
            if sePuedeGirar:
                self.angulo -= ang
                tiempo = ((ang * math.pi / 180) / self.velocidad)
                print('\nGirando articulación...')
                time.sleep(tiempo)
                return True
            else:
                return False
        elif (sen == 'A'):
            sePuedeGirar = (self.angulo + ang) <= self.anguloMaximo
            if sePuedeGirar:
                self.angulo += ang
                tiempo = ((ang * math.pi / 180) / self.velocidad)
                print('\nGirando articulación...')
                time.sleep(tiempo)
                return True
            else:
                return False
        else:
            return False

    def setVelocidad(self, velocidad):
        vel = float(velocidad)
        if (vel > self.velocidadMaxima or vel < self.velocidadMinima):
            return False
        self.velocidad = vel
        return True
