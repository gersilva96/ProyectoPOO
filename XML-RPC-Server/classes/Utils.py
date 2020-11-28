import os

class Utils():

    def __init__(self):
        self.hola = 'hola'

    def init(self):
        os.system('clear')
        print('*' + '-'*70 + '*')
        print(
            '|' + '{:^70}'.format('Programación Orientada a Objetos 2020') + '|')
        print(
            '|' + '{:^70}'.format('Intefaz de control servidor Robot-RRR') + '|')
        print('|' + '{:^70}'.format('') + '|')
        print('|' + '{:>70}'.format('Wieckowski, Martín - Silva, Germán') + '|')
        print('|' + '{:^70}'.format('') + '|')
        print(
            '|' + '{:<70}'.format('Utilice el comando \'help\' para obtener ayuda del sistema.') + '|')
        print('*' + '-'*70 + '*\n')

    def printOptions(self, options):
        print('\nIngrese una de las siguientes opciones:\n')
        for key in options:
            print(key + ': ' + options[key])
        print('')

utils = Utils()
