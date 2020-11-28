import time


class EfectorFinal():

    def __init__(self, id, nombre, estado=False):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getEstado(self):
        return self.estado

    def setEstado(self, tiempo):
        tmp = float(tiempo)
        self.estado = True
        time.sleep(tmp)
        self.estado = False
