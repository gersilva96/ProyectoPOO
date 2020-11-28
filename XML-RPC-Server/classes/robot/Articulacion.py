class Articulacion():

    def __init__(self, id, nombre, anguloMinimo, anguloMaximo, velocidadMaxima):
        self.id = id
        self.nombre = nombre
        self.angulo = 0.0
        self.anguloInicial = 0.0
        self.anguloMinimo = anguloMinimo
        self.anguloMaximo = anguloMaximo
        self.velocidad = 1.0
        self.velocidadInicial = 1.0
        self.velocidadMinima = 0.1
        self.velocidadMaxima = velocidadMaxima

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAngulo(self):
        return self.angulo

    def getVelocidad(self):
        return self.velocidad

    def setAngulo(self, sen, ang):
        sentido, angulo = str(sen).upper(), float(ang)
        if (sentido == 'H'):
            sePuedeGirar = (self.angulo - angulo) >= self.anguloMinimo
            if sePuedeGirar:
                self.angulo -= angulo
                return True
            else:
                return False
        elif (sentido == 'A'):
            sePuedeGirar = (self.angulo + angulo) <= self.anguloMaximo
            if sePuedeGirar:
                self.angulo += angulo
                return True
            else:
                return False
        else:
            return False

    def setVelocidad(self, vel):
        velocidad = float(vel)
        if (velocidad > self.velocidadMaxima or velocidad < self.velocidadMinima):
            return False
        self.velocidad = velocidad
        return True
