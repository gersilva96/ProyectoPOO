from classes.robot.Robot import Robot
import time

rob = Robot()

print("\nEjecutando el modo de prueba...\n")
print("Moviendo la articulación base, 20° a 3 rad/s en sentido horario")
if rob.articulacion1.setAngulo(20, True) == False:
  time.sleep(3)
  print("Articulación rotada con éxito")
else:
  print("Angulo de articulación excedio")

print("\nMoviendo la articulación media, 15° a 1 rad/s en sentido antihorario")
if rob.articulacion2.setAngulo(15, False) == False:
  time.sleep(3)
  print("Articulación rotada con éxito")
else:
  print("Angulo de articulación excedio")

print("\nMoviendo la articulación final, 5° a 3 rad/s en sentido horario")
if rob.articulacion3.setAngulo(5, True) == False:
  time.sleep(3)
  print("Articulación rotada con éxito")
else:
  print("Angulo de articulación excedio")


print("\nIntentamos de mover la articulación final 90°")
if rob.articulacion3.setAngulo(90, True) == False:
  time.sleep(3)
  print("Articulación rotada con éxito")
else:
  time.sleep(3)
  print("Angulo de articulación excedio!!!")

print("\nIntentamos mover la articulación de la base a 200 rad/s")
if rob.articulacion1.setVelocidad(200) == False:
  time.sleep(3)
  print("Articulación rotada con éxito")
else:
  time.sleep(3)
  print("Velocidad de la articulación excedida!!!")

print("\nActivamos el efector final durante 5 segundos")
rob.EfectorFinal(5)
print("Efector activado con éxito")

print("\n\n*************Modo de prueba finalizado***************\n\n")





