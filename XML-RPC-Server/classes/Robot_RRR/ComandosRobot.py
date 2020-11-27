from cmd import Cmd 
from classes.Robot_RRR.RobotRRR import Robot
import time

###### Este archivo sirve únicamente para el modo manual del servidor ##############

class ComandosR(Cmd):
    doc_header = "Comandos documentados"
    ruler = "*"  
            
    def do_quit(self, args):
        """Vuelve al menú"""
        print("Ejecución finalizada")
        raise SystemExit
    
    def default(self, args):
        print("Error. El comando \'" + args + "\' no esta disponible")

    def precmd(self, args):
        args = args.lower()
        return(args) 

    def do_ma(self, args):
        """Mueve una articulación. Recibe como parámetros el ángulo de rotación, la velocidad angular, y el sentido de rotación del ángulo"""
        robot=Robot()
        print("\nArticulación de la base------1\nArticulación media-----------2\nArticulación superior--------3\n")
        res = int(input())
        if res == 1:
            flag=True
            while flag:
              print("Ingrese Angulo de rotacion")
              a1 = input()
              print("Ingrese sentido de rotacion(Horario: H , Antihorario: A): ")
              b1 = str(input())
              if b1 == "H":
                flag = robot.articulacion1.setAngulo(a1, True)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              elif b1 == "A":
                flag = robot.articulacion1.setAngulo(a1, False)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              else: 
                flag = True
            flag2=True
            while flag2:
              print("Ingrese velocidad angular")
              c1 = float(input())
              flag2 = robot.articulacion1.setVelocidad(c1)
              if flag2 == True:
                  print("\n\n********Velocidad excedida**********\n\n")
            print("Moviendo articulación...")
            time.sleep(3)
            print("Articulación rotada con éxito")

        if res == 2:
            flag=True
            while flag:
              print("Ingrese Angulo de rotacion")
              a2 = input()
              print("Ingrese sentido de rotacion(Horario: H , Antihorario: A): ")
              b2 = str(input())
              if b2 == "H":
                flag = robot.articulacion2.setAngulo(a2, True)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              elif b2 == "A":
                flag = robot.articulacion2.setAngulo(a2, False)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              else: 
                flag = True
            flag2=True
            while flag2:
              print("Ingrese velocidad angular")
              c2 = float(input())
              flag2 = robot.articulacion2.setVelocidad(c2)
              if flag2 == True:
                  print("\n\n********Velocidad excedida**********\n\n")
            print("Moviendo articulación...")
            time.sleep(3)
            print("Articulación rotada con éxito")

        if res == 3:
            flag=True
            while flag:
              print("Ingrese Angulo de rotacion")
              a3 = input()
              print("Ingrese sentido de rotacion(Horario: H , Antihorario: A): ")
              b3 = str(input())
              if b3 == "H":
                flag = robot.articulacion3.setAngulo(a3, True)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              elif b3 == "A":
                flag = robot.articulacion3.setAngulo(a3, False)
                if flag == True:
                  print("\n\n************Capacidad de la articulacion eccedida***********\n\n")
              else: 
                flag = True
            flag2=True
            while flag2:
              print("Ingrese velocidad angular")
              c3 = float(input())
              flag2 = robot.articulacion3.setVelocidad(c3)
              if flag2 == True:
                  print("\n\n********Velocidad excedida**********\n\n")
            print("Moviendo articulación...")
            time.sleep(3)
            print("Articulación rotada con éxito")



    def do_aef(self, args):
        """Activa el efector final por un tiempo determinado. Recibe como parámetro el tiempo en segundos"""
        robot=Robot()
        print("Ingrese tiempo de actuación del efector final(en segundos): ")
        tiempo = int(input())
        robot.EfectorFinal(tiempo)
        

    def do_vao(self, args):
        """Volver al origen: Regresa el dispositivo a su posición original"""
        robot=Robot()
        robot.articulacion1.setAngulo(0, True)
        robot.articulacion2.setAngulo(0, True)
        robot.articulacion3.setAngulo(0, True)
        time.sleep(3)
        print("El dispositivo volvió a su posición original")
        


