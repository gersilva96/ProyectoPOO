from classes.XmlRpcServer import XmlRpcServer
from classes.Comandos import Comandos

print("\nBienvenido al proyecto de Programación Orientada a Objetos 2020 \n")
print("¿Qué desea hacer?\n")
print("Ver manual de instrucciones---------1\nConectar con el robot---------------2\n")
res1 = int(input())
if res1 == 1:
	print("Sección de ayuda de comandos.Introduzca help para ver los comandos documentados\n")
	Comandos.prompt = 'Esperando Instruccion: '
	Comandos().cmdloop()

if res1 == 2:
	print("\nConectando con el robot...")
	print("Conección exitosa")
	print("¿En que modo desea trabajar?\n")
	print("Modo manual----------------------------------1\nEsperar insturcciones del cliente------------2 \nIniciar simulación de prueba-----------------3\n")
	res2 = int(input())
	if res2 == 1:
		print("a")
	if res2 == 2:
		print("Lanzando servidor...\n")
		obj = Comandos
		servidor = XmlRpcServer()
	if res2 == 3:
		print("Ejecutando archivo de prueba")
