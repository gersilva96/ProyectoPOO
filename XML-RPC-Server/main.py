from classes.XmlRpcServer import XmlRpcServer
from classes.Comandos import Comandos

print("\nBienvenido al proyecto de Programación Orientada a Objetos 2020 \n")
print("¿Qué desea hacer?\n")
print("Ver manual de instrucciones------------------1\nConectar con el robot------------------------2\nModo manual----------------------------------3\nEsperar insturcciones del cliente------------4 \nIniciar simulación de prueba-----------------5\n")
res1 = int(input())
if res1 == 1:
	print("Sección de ayuda de comandos.Introduzca help para ver los comandos documentados\n")
	Comandos.prompt = 'Esperando Instruccion: '
	Comandos().cmdloop()

if res1 == 2:
	print("\nConectando con el robot...")
	print("Conección exitosa")
	#Conectar con la funcion Robot
if res2 == 3:
	print("Iniciando modo manual")
	#Conectar con la funcion Robot
if res2 == 4:
		print("Lanzando servidor...\n")
		obj = Comandos
		servidor = XmlRpcServer()
if res2 == 5:
		print("Ejecutando archivo de prueba")