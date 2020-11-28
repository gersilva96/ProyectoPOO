class Logger():

    def __init__(self, robot):
        self.robot = robot

    def anguloArticulacion(self, articulacion, sentido, angulo):
        art, sen, ang = int(articulacion), str(sentido), float(angulo)
        sentidoGiro = ''
        if (sen == 'A'):
            sentidoGiro = 'antihorario'
        elif (sen == 'H'):
            sentidoGiro = 'horario'
        with open('log.txt', 'a') as f:
            f.write('La articulación \'' + str(self.robot.getNombreArt(art)) + '\' rotó ' + str(ang) + '° en sentido ' + str(sentidoGiro) + '\n')

    def velocidadArticulacion(self, articulacion, velocidad):
        art, vel = int(articulacion), float(velocidad)
        with open('log.txt', 'a') as f:
            f.write('Se cambió la velocidad angular de la articulación \'' + str(self.robot.getNombreArt(art)) + '\' a ' + str(vel) + ' rad/s\n')

    def estadoEfectorFinal(self, tiempo):
        tmp = float(tiempo)
        with open('log.txt', 'a') as f:
            f.write('Se accionó el efector final durante ' + str(tmp) + ' segundos\n')
